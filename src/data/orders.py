from data import SessionData
from db.entity.dish import Dish as DishDB
from db.entity.order import Order as OrderDB
from db.entity.restaurant import Restaurant as RestaurantDB
from db.entity.order_dish import OrderDish as OrderDishDB
from db.entity.dining_table import DiningTable as DiningTableDB
from db.enums.enum import OrderType, OrderStatus


class Orders(SessionData):

    def get_order(self, order_id: int):
        try:
            order = self.session.query(OrderDB).get(order_id)
            if order is None:
                raise ValueError("No resource found")
            return {
                "id": order.id,
                "order_type": order.order_type.name,
                "restaurant_id": order.restaurant_id,
                "restaurant_name": self.get_restaurant_name(order.restaurant_id),
                "dining_table_id": order.dining_table_id,
                "dining_table_no": self.get_table_no(order.dining_table_id) if order.dining_table_id else None,
                "dish_items": self.get_dish_items(order.id),
                "special_message": order.special_message,
                "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": order.modified_at.strftime("%Y-%m-%d %H:%M:%S") if order.modified_at else None,
                "created_by": order.created_by,
                "modified_by": order.modified_by,
            }
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def get_restaurant_name(self, restaurant_id: int):
        return self.session.query(RestaurantDB).get(restaurant_id).name

    def get_table_no(self, dining_table_id: int):
        return self.session.query(DiningTableDB).get(dining_table_id).table_no

    def get_dish_items(self, order_id: int):
        dish_items = [
            dish_item.dish_id for dish_item in self.session.query(OrderDishDB).join(DishDB).filter(OrderDishDB.order_id==order_id).all()
        ]
        dish_items = [dish_item.name for dish_item in self.session.query(DishDB).filter(DishDB.id.in_(dish_items))]
        return dish_items

    def get_orders(self):
        try:
            orders = self.session.query(OrderDB).all()
            return [{
                "id": order.id,
                "order_type": order.order_type.name,
                "restaurant_id": order.restaurant_id,
                "restaurant_name": self.get_restaurant_name(order.restaurant_id),
                "dining_table_id": order.dining_table_id,
                "dining_table_no": self.get_table_no(order.dining_table_id) if order.dining_table_id else None,
                "dish_items": self.get_dish_items(order.id),
                "special_message": order.special_message,
                "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": order.modified_at.strftime("%Y-%m-%d %H:%M:%S") if order.modified_at else None,
                "created_by": order.created_by,
                "modified_by": order.modified_by,
            } for order in orders]
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def validate_dish_orders(self, dish_items: list):
        errors = []
        for dish_id in dish_items:
            if self.session.query(DishDB).get(dish_id) is None:
                errors.append({"error": f"Invalid dish id : '{dish_id}' "})
        return errors

    def validate_restaurant_id(self, restaurant_id: int):
        return self.session.query(RestaurantDB).get(restaurant_id)

    def validate_dining_table(self, dining_table_id: int, restaurant_id: int):
        return self.session.query(DiningTableDB).filter(DiningTableDB.id==dining_table_id, DiningTableDB.restaurant_id==restaurant_id).first()

    def create_order(self, data: dict):
        try:
            dish_items = data["dish_items"]
            data.pop("dish_items")

            order_obj = OrderDB(
                order_type=OrderType(data["order_type"]).name,
                status=OrderStatus(data["order_status"]).name,
                special_message=data["special_message"],
                dining_table_id=data["dining_table_id"],
                restaurant_id=data["restaurant_id"],
                created_by=data["created_by"]
            )
            self.session.add(order_obj)
            self.session.commit()
            self.session.refresh(order_obj)
            dish_items = [OrderDishDB(order_id=order_obj.id, dish_id=dish_id) for dish_id in dish_items]
            self.session.add_all(dish_items)
            self.session.commit()
            self.session.refresh(order_obj)
            return order_obj
        except ValueError as e:
            return {"error": str(e)}

    def update_order(self, order_id: int, data: dict):
        try:
            dish_items = data["dish_items"]
            data.pop("dish_items")

            order_obj = self.session.query(OrderDB).get(order_id)
            if order_obj is None:
                raise ValueError("No resource found")
            order_obj.order_type = OrderType(data["order_type"]).name
            order_obj.status = OrderStatus(data["order_status"]).name
            data.pop("order_type")
            data.pop("order_status")
            for key, value in data.items():
                setattr(order_obj, key, value)
            self.session.commit()
            self.session.refresh(order_obj)

            for order_dish in self.session.query(OrderDishDB).filter_by(order_id=order_id):
                self.session.delete(order_dish)
            self.session.commit()

            dish_items = [OrderDishDB(order_id=order_obj.id, dish_id=dish_id) for dish_id in dish_items]
            self.session.add_all(dish_items)
            self.session.commit()

            self.session.refresh(order_obj)
            return order_obj
        except ValueError as e:
            return {"error": str(e)}

    def delete_order(self, order_id: int):
        try:
            order_obj = self.session.query(OrderDB).get(order_id)
            if order_obj is None:
                raise ValueError("No resource found")
            self.session.delete(order_obj)
            for order_dish in self.session.query(OrderDishDB).filter_by(order_id=order_id):
                self.session.delete(order_dish)
        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

        else:
            self.session.commit()
            return True

from flask import g
from data.orders import Orders as OrdersData
from db.enums.enum import OrderType, OrderStatus


class Orders:
    """
    Action class for DiningTable
    """

    @staticmethod
    def get_order(order_id: int):
        return OrdersData().get_order(order_id)

    @staticmethod
    def get_orders():
        return OrdersData().get_orders()

    @staticmethod
    def create_order(data: dict):
        try:
            data.update({
                "created_by": g.user_id
            })

            OrderType(data["order_type"])  # just for validating the enum for valid type
            OrderStatus(data["order_status"])  # just for validating the enum for valid type

            order_item = OrdersData()

            if not data["dish_items"]:
                raise ValueError("dish_items shouldn't empty .")

            if order_item.validate_restaurant_id(data["restaurant_id"]) is None:
                raise ValueError("Invalid restaurant_id.")

            if data["order_type"] == 2:

                if data.get("dining_table_id") is None:
                    raise ValueError(f"dining_table_id is required for order type : '{OrderType(2).name}' .")

                if order_item.validate_dining_table(data["dining_table_id"], data["restaurant_id"]) is None:
                    raise ValueError("Invalid dining_table_id.")
            else:
                data.update({"dining_table_id": None})

            validated_dish_result = order_item.validate_dish_orders(data["dish_items"])
            if validated_dish_result:
                return validated_dish_result
            return order_item.create_order(data)
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update_order(order_id: int, data: dict):
        try:
            if not data:
                return {"error": "Please provide at least one field for updation"}
            data.update({
                "modified_by": g.user_id,
            })

            OrderType(data["order_type"])  # just for validating the enum for valid type
            OrderStatus(data["order_status"])  # just for validating the enum for valid type

            order_item = OrdersData()

            if not data["dish_items"]:
                raise ValueError("dish_items shouldn't empty .")

            if order_item.validate_restaurant_id(data["restaurant_id"]) is None:
                raise ValueError("Invalid restaurant_id.")

            if data["order_type"] == 2:

                if data.get("dining_table_id") is None:
                    raise ValueError(f"dining_table_id is required for order type : '{OrderType(2).name}' .")

                if order_item.validate_dining_table(data["dining_table_id"], data["restaurant_id"]) is None:
                    raise ValueError("Invalid dining_table_id.")
            else:
                data.update({"dining_table_id": None})

            validated_dish_result = order_item.validate_dish_orders(data["dish_items"])
            if validated_dish_result:
                return validated_dish_result
            return order_item.update_order(order_id, data)
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete_order(order_id: int):
        return OrdersData().delete_order(order_id)

from data import SessionData
from db.entity.tag import Tag as TagDB
from db.entity.dish import Dish as DishDB
from db.entity.dish_tag import DishTag as DishTagDB
from db.entity.restaurant import Restaurant as RestaurantDB
from db.enums.enum import TagType


class Dish(SessionData):

    def get_dish_tags(self, dish_id: int):
        tags = self.session.query(TagDB).join(DishTagDB).filter(DishTagDB.dish_id == dish_id).all()
        return [tag.name for tag in tags]

    def get_dish_item(self, dish_id):
        try:
            dish_item = self.session.query(DishDB, RestaurantDB).join(RestaurantDB).filter(
                DishDB.id == dish_id).first()
            if dish_item is None:
                raise ValueError("No resource found")
            dish_item, restaurant = dish_item
            return {
                "id": dish_item.id,
                "name": dish_item.name,
                "description": dish_item.description,
                "availability": dish_item.availability,
                "restaurant_id": restaurant.name,
                "tags": self.get_dish_tags(dish_item.id),
                "created_at": dish_item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": dish_item.modified_at.strftime("%Y-%m-%d %H:%M:%S") if dish_item.modified_at else None,
                "created_by": dish_item.created_by,
                "modified_by": dish_item.modified_by,
            }
        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

    def get_dish_items(self):
        try:
            dish_items = self.session.query(DishDB, RestaurantDB).join(RestaurantDB).all()
            if dish_items is None:
                raise ValueError("No resources found")
            return [{
                "id": dish_item.id,
                "name": dish_item.name,
                "description": dish_item.description,
                "availability": dish_item.availability,
                "restaurant_id": restaurant.name,
                "tags": self.get_dish_tags(dish_item.id),
                "created_at": dish_item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": dish_item.modified_at.strftime(
                    "%Y-%m-%d %H:%M:%S") if dish_item.modified_at else None,
                "created_by": dish_item.created_by,
                "modified_by": dish_item.modified_by,
            } for dish_item, restaurant in dish_items]
        except Exception as e:
            return {"error": str(e)}

    def validate_restaurant(self, restaurant_id: int):
        return self.session.query(RestaurantDB).get(restaurant_id)

    def validate_tags(self, tags: list):
        error_tags = []
        for tag in tags:
            if self.session.query(TagDB).filter(TagDB.type == TagType(2).name, TagDB.id == tag).first() is None:
                error_tags.append({"error": f"Invalid dish tag id '{tag}'."})
        return error_tags

    def create_dish(self, data: dict):
        try:
            tags = data["tags"]
            data.pop("tags")
            dish_item = DishDB(**data)
            self.session.add(dish_item)
            self.session.commit()
            self.session.refresh(dish_item)
            tags = [DishTagDB(dish_id=dish_item.id, tag_id=tag_id) for tag_id in tags]
            self.session.add_all(tags)
            self.session.commit()
            self.session.refresh(dish_item)
            return dish_item
        except Exception as e:
            return {"error": str(e)}

    def update_dish(self, dish_id: int, data: dict):
        try:
            dish_obj = self.session.query(DishDB).get(dish_id)
            if dish_obj is None:
                raise ValueError("No resource found")

            if data.get("tags"):
                for tag in self.session.query(DishTagDB).filter_by(dish_id=dish_obj.id):
                    self.session.delete(tag)
                self.session.commit()

                dish_tags = [DishTagDB(dish_id=dish_obj.id, tag_id=tag) for tag in data["tags"]]
                self.session.add_all(dish_tags)
                self.session.commit()

                data.pop("tags")

            for key, value in data.items():
                setattr(dish_obj, key, value)
            self.session.commit()
            self.session.refresh(dish_obj)
            return dish_obj
        except ValueError:
            return {
                "error": "No resource found"
            }

    def delete_dish(self, dish_id):
        try:
            dish_obj = self.session.query(DishDB).get(dish_id)
            if dish_obj is None:
                raise ValueError("No resource found")
            for tags in self.session.query(DishTagDB).filter_by(dish_id=dish_obj.id):
                self.session.delete(tags)
            self.session.commit()
            self.session.delete(dish_obj)
            self.session.commit()
            return True

        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

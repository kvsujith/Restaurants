from flask import g
from utils.utils import get_indian_time
from data.dish import Dish as DishData


class Dish:
    """
    Action class for Dish
    """

    @staticmethod
    def get_dish_item(dish_id: int):
        return DishData().get_dish_item(dish_id)

    @staticmethod
    def get_dish_items():
        return DishData().get_dish_items()

    @staticmethod
    def create_dish(data: dict):
        data.update({
            "created_by": g.user_id
        })
        dish_data = DishData()
        if dish_data.validate_restaurant(data["restaurant_id"]) is None:
            return {"error": f"Invalid restaurant id '{data['restaurant_id']}' "}

        dish_tags = dish_data.validate_tags(data["tags"])
        if dish_tags:
            return dish_tags

        return dish_data.create_dish(data)

    @staticmethod
    def update_dish(dish_id: int, data: dict):
        if not data:
            return {"error": "Please provide at least one field for updation"}
        data.update({
            "modified_by": g.user_id,
            "modified_at": get_indian_time(),
        })
        dish_data = DishData()

        if data.get("restaurant_id"):
            if dish_data.validate_restaurant(data["restaurant_id"]) is None:
                return {"error": f"Invalid restaurant id '{data['restaurant_id']}' "}

        if data.get("tags"):
            dish_tags = dish_data.validate_tags(data["tags"])
            if dish_tags:
                return dish_tags

        return dish_data.update_dish(dish_id, data)

    @staticmethod
    def delete_dish(dish_id: int):
        return DishData().delete_dish(dish_id)

"""actions file for Restaurant"""
from flask import g
from utils.utils import get_indian_time
from data.restaurant import Restaurant as RestaurantData


class Restaurant:

    @staticmethod
    def create_restaurant(data):
        data.update({
            "created_at": get_indian_time(),
            "created_by": g.user_id
        })
        restaurant_data = RestaurantData()
        restaurant_data = restaurant_data.create_restaurant(data)
        return restaurant_data

    @staticmethod
    def update_restaurant(restaurant_id, data):
        data.update({
            "modified_at": get_indian_time(),
            "modified_by": g.user_id
        })
        try:
            restaurant_data = RestaurantData()
            restaurant_data = restaurant_data.update_restaurant(restaurant_id, data)
            return restaurant_data
        except ValueError:
            return {
                "error": "Something went wrong"
            }

    @staticmethod
    def delete_restaurant(_id):
        return RestaurantData().delete_restaurant(_id)

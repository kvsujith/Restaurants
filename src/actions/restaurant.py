"""actions file for Restaurant"""
import datetime

from flask import g
from data.restaurant import Restaurant as RestaurantData


class Restaurant:

    @staticmethod
    def get_restaurant(restaurant_id):
        data_obj = RestaurantData()
        restaurant_data = data_obj.get_restaurant(restaurant_id)
        if isinstance(restaurant_data, dict):
            return restaurant_data
        return {
            "id": restaurant_data.id,
            "name": restaurant_data.name,
            "description": restaurant_data.description,
            "locations": data_obj.get_restaurant_locations(restaurant_data.id),
            "tags": data_obj.get_restaurant_tags(restaurant_data.id),
            "created_at": restaurant_data.created_at.strftime(
                "%Y-%m-%d %H:%M:%S") if restaurant_data.created_at else None,
            "modified_at": restaurant_data.modified_at.strftime(
                "%Y-%m-%d %H:%M:%S") if restaurant_data.modified_at else None,
            "created_by": restaurant_data.created_by,
            "modified_by": restaurant_data.modified_by,
        }

    @staticmethod
    def get_restaurants():
        return RestaurantData().get_restaurants()

    @staticmethod
    def create_restaurant(data):

        data.update({
            "created_by": g.user_id
        })
        restaurant_data = RestaurantData()
        validate_tag_result = restaurant_data.validate_tags(data["tags"])
        validate_location_result = restaurant_data.validate_locations(data["locations"])
        if validate_tag_result:
            return validate_tag_result
        if validate_location_result:
            return validate_location_result
        restaurant_data = restaurant_data.create_restaurant(data)
        return restaurant_data

    @staticmethod
    def update_restaurant(restaurant_id, data):
        data.update({
            "modified_by": g.user_id,
            "modified_at": datetime.datetime.now(),
        })

        restaurant_data = RestaurantData()

        validate_tag_result = restaurant_data.validate_tags(data["tags"])
        validate_location_result = restaurant_data.validate_locations(data["locations"])

        if validate_tag_result:
            return validate_tag_result
        if validate_location_result:
            return validate_location_result

        restaurant_data = restaurant_data.update_restaurant(restaurant_id, data)
        return restaurant_data

    @staticmethod
    def delete_restaurant(_id):
        return RestaurantData().delete_restaurant(_id)

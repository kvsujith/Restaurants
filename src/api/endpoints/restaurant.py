from flask import request
from data import SessionData
from flask_restx import Resource
from api.namespaces import restaurant
from utils.utils import get_json_data
from actions.restaurant import Restaurant as RestaurantAction
from db.entity.restaurant import Restaurant as RestaurantDB
from api.models.restaurant import restaurant_model, restaurant_view


@restaurant.route("")
class Restaurant(Resource):

    @staticmethod
    def get():
        return RestaurantAction.get_tags()

    @staticmethod
    @restaurant.expect(restaurant_model, validate=True)
    def post():
        data = request.get_json()
        restaurant_obj = RestaurantAction()
        restaurant_obj = restaurant_obj.create_restaurant(data)
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": restaurant_obj.id},
        }
        return response, 201


@restaurant.route("/update/<int:token>")
class UpdateRestaurant(Resource):

    @staticmethod
    @restaurant.expect(restaurant_model, validate=True)
    def put(token):
        data = request.get_json()
        restaurant_obj = RestaurantAction()
        restaurant_obj = restaurant_obj.update_restaurant(token, data)
        if isinstance(restaurant_obj, dict):
            return restaurant_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": restaurant_obj.id},
        }
        return response, 201


@restaurant.route("/delete/<int:token>")
class DeleteRestaurant(Resource):

    @staticmethod
    def delete(token):
        restaurant_obj = RestaurantAction().delete_restaurant(token)
        if restaurant_obj:
            response = {
                "status": "SUCCESS",
                "code": 0,
                "message": "MESSAGE_DELETED",
            }
            return response, 204
        return {"error": "No resource found"}

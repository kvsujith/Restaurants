from flask import request
from flask_restx import Resource
from api.namespaces import restaurant
from api.models.restaurant import restaurant_model
from actions.restaurant import Restaurant as RestaurantAction


@restaurant.route("")
class Restaurant(Resource):

    @staticmethod
    def get():
        restaurants = RestaurantAction()
        restaurants = restaurants.get_restaurants()
        if isinstance(restaurants, dict):
            return restaurants, 400
        return restaurants

    @staticmethod
    @restaurant.expect(restaurant_model, validate=True)
    def post():
        data = request.get_json()
        restaurant_obj = RestaurantAction()
        restaurant_obj = restaurant_obj.create_restaurant(data)
        if isinstance(restaurant_obj, (dict, list)):
            return restaurant_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": restaurant_obj.id},
        }
        return response, 201


@restaurant.route("/<int:restaurant_id>")
class GETRestaurant(Resource):

    @staticmethod
    def get(restaurant_id):
        restaurants = RestaurantAction()
        restaurants = restaurants.get_restaurant(restaurant_id)
        if isinstance(restaurants, dict) and restaurants.get("error"):
            return restaurants, 400
        return restaurants


@restaurant.route("/update/<int:restaurant_id>")
class UpdateRestaurant(Resource):

    @staticmethod
    @restaurant.expect(restaurant_model, validate=True)
    def put(restaurant_id):
        data = request.get_json()
        restaurant_obj = RestaurantAction()
        restaurant_obj = restaurant_obj.update_restaurant(restaurant_id, data)
        if isinstance(restaurant_obj, (dict, list)):
            return restaurant_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": restaurant_obj.id},
        }
        return response, 200


@restaurant.route("/delete/<int:restaurant_id>")
class DeleteRestaurant(Resource):

    @staticmethod
    def delete(restaurant_id):
        restaurant_obj = RestaurantAction().delete_restaurant(restaurant_id)
        if restaurant_obj:
            response = {
                "status": "SUCCESS",
                "code": 0,
                "message": "MESSAGE_DELETED",
            }
            return response, 204
        return {"error": "No resource found"}

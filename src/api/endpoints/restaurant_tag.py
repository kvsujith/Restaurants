from flask import request
from flask_restx import Resource
from api.namespaces import restaurant_tag
from api.models.restaurant_tag import restaurant_tag_model
from actions.restaurant_tag import RestaurantTag as RestaurantTagAction


@restaurant_tag.route("")
class RestaurantTag(Resource):

    @staticmethod
    def get():
        return RestaurantTagAction.get_restaurant_tag_data()

    @staticmethod
    @restaurant_tag.expect(restaurant_tag_model, validate=True)
    def post():
        data = request.get_json()
        restaurant_tag_obj = RestaurantTagAction()
        restaurant_tag_obj = restaurant_tag_obj.create_restaurant_tag(data)
        if isinstance(restaurant_tag_obj, dict):
            return restaurant_tag_obj
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": restaurant_tag_obj.id},
        }
        return response, 201


@restaurant_tag.route("/update/<int:restaurant_tag_id>")
class UpdateRestaurantTag(Resource):

    @staticmethod
    @restaurant_tag.expect(restaurant_tag_model, validate=True)
    def put(restaurant_tag_id):
        data = request.get_json()
        restaurant_obj = RestaurantTagAction()
        restaurant_obj = restaurant_obj.update_restaurant_tag(restaurant_tag_id, data)
        if isinstance(restaurant_obj, dict):
            return restaurant_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": restaurant_obj.id},
        }
        return response, 201


@restaurant_tag.route("/delete/<int:restaurant_tag_id>")
class DeleteRestaurantTag(Resource):

    @staticmethod
    def delete(restaurant_tag_id):
        restaurant_obj = RestaurantTagAction().delete_restaurant_tag(restaurant_tag_id)
        if isinstance(restaurant_obj, dict):
            return restaurant_obj
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204


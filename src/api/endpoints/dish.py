from flask import request
from api.namespaces import dish
from flask_restx import Resource
from api.models.dish import dish_model
from actions.dish import Dish as DishAction


@dish.route("")
class Dish(Resource):

    @staticmethod
    def get():
        dish_item = DishAction()
        return dish_item.get_dish_items()

    @staticmethod
    @dish.expect(dish_model, validate=True)
    def post():
        data = request.get_json()
        dish_item = DishAction()
        dish_item = dish_item.create_dish(data)
        if isinstance(dish_item, (dict, list)):
            return dish_item, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": dish_item.id},
        }
        return response, 201


@dish.route("/<int:dish_id>")
class GetDish(Resource):

    @staticmethod
    def get(dish_id: int):
        dish_item = DishAction().get_dish_item(dish_id)
        if dish_item.get("error"):
            return dish_item, 400
        return dish_item


@dish.route("/update/<int:dish_id>")
class UpdateDish(Resource):

    @staticmethod
    @dish.expect(dish_model, validate=False)
    def put(dish_id: int):
        data = request.get_json()
        dish_update = DishAction()
        dish_update = dish_update.update_dish(dish_id, data)
        if isinstance(dish_update, (dict, list)):
            return dish_update, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": dish_update.id},
        }
        return response, 200


@dish.route("/delete/<int:dish_id>")
class DeleteDish(Resource):

    @staticmethod
    def delete(dish_id: int):
        dish_obj = DishAction()
        dish_obj = dish_obj.delete_dish(dish_id)
        if isinstance(dish_obj, dict):
            return dish_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204

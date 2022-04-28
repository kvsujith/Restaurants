from flask import request
from flask_restx import Resource
from api.namespaces import dining_table
from api.models.dining_table import dining_table_model
from actions.dining_table import DiningTable as DiningTableAction


@dining_table.route("")
class DiningTable(Resource):

    @staticmethod
    def get():

        return []

    @staticmethod
    @dining_table.expect(dining_table_model, validate=True)
    def post():
        data = request.get_json()
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": data},
        }
        return response, 201


@dining_table.route("/<int:dining_table_id>")
class GetDiningTable(Resource):

    @staticmethod
    def get(dining_table_id: int):
        dining_obj = DiningTableAction.get_dining_table(dining_table_id)
        if dining_obj.get("error"):
            return dining_obj, 400
        return dining_obj


@dining_table.route("/update/<int:dining_table_id>")
class UpdateDiningTable(Resource):

    @staticmethod
    @dining_table.expect(dining_table_model, validate=False)
    def put(dining_table_id: int):
        data = request.get_json()

        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": data},
        }
        return response, 200


@dining_table.route("/delete/<int:dining_table_id>")
class DeleteDiningTable(Resource):

    @staticmethod
    def delete(dining_table_id: int):
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204

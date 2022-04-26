from flask import request
from flask_restx import Resource
from api.namespaces import location
from api.models.location import location_model
from actions.location import Location as LocationAction


@location.route("")
class Location(Resource):

    @staticmethod
    def get():
        return LocationAction.get_locations()

    @staticmethod
    @location.expect(location_model, validate=True)
    def post():
        try:
            data = request.get_json()
            location_obj = LocationAction()
            location_obj = location_obj.create_location(data)
            if isinstance(location_obj, dict):
                return location_obj
            response = {
                "status": "SUCCESS",
                "code": 0,
                "message": "MESSAGE_CREATED",
                "result": {"id": location_obj.id},
            }
            return response, 201
        except Exception as e:
            return {"error": str(e)}


@location.route("/<int:location_id>")
class Location(Resource):

    @staticmethod
    def get(location_id):
        return LocationAction.get_location(location_id)


@location.route("/update/<int:location_id>")
class UpdateLocation(Resource):

    @staticmethod
    @location.expect(location_model, validate=True)
    def put(location_id):
        data = request.get_json()
        location_obj = LocationAction()
        location_obj = location_obj.update_location(location_id, data)
        if isinstance(location_obj, dict):
            return location_obj
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": location_obj.id},
        }
        return response, 201


@location.route("/delete/<int:location_id>")
class DeleteLocation(Resource):

    @staticmethod
    def delete(location_id):
        location_obj = LocationAction()
        location_obj = location_obj.delete_location(location_id)
        if isinstance(location_obj, dict):
            return location_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204

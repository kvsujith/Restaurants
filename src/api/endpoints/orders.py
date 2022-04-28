from flask import request
from flask_restx import Resource
from api.namespaces import orders
from api.models.orders import orders_model
from actions.orders import Orders as OrdersAction


@orders.route("")
class Orders(Resource):

    @staticmethod
    def get():
        order_action = OrdersAction.get_orders()
        if isinstance(order_action, dict):
            return order_action, 400
        return order_action

    @staticmethod
    @orders.expect(orders_model, validate=True)
    def post():
        data = request.get_json()
        order_obj = OrdersAction.create_order(data)
        if isinstance(order_obj, (dict, list)):
            return order_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": order_obj.id},
        }
        return response, 201


@orders.route("/<int:order_id>")
class GetDiningTable(Resource):

    @staticmethod
    def get(order_id: int):
        order_action = OrdersAction.get_order(order_id)
        if isinstance(order_action, dict):
            return order_action, 400
        return order_action


@orders.route("/update/<int:order_id>")
class UpdateDiningTable(Resource):

    @staticmethod
    @orders.expect(orders_model, validate=False)
    def put(order_id: int):
        data = request.get_json()
        order_obj = OrdersAction.update_order(order_id, data)
        if isinstance(order_obj, dict):
            return order_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": order_obj.id},
        }
        return response, 200


@orders.route("/delete/<int:order_id>")
class DeleteDiningTable(Resource):

    @staticmethod
    def delete(order_id: int):
        order_obj = OrdersAction().delete_order(order_id)
        if isinstance(order_obj, dict):
            return order_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204

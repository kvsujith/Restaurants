from flask import request
from flask_restx import Resource
from api.namespaces import customer
from api.models.customer import customer_model
from actions.customer import Customer as CustomerAction


@customer.route("")
class Customer(Resource):

    @staticmethod
    def get():
        customers = CustomerAction.get_customers()
        if isinstance(customers, dict):
            return customers, 400
        return customers

    @staticmethod
    @customer.expect(customer_model, validate=True)
    def post():
        data = request.get_json()
        customer_obj = CustomerAction()
        customer_obj = customer_obj.create_customer(data)
        if isinstance(customer_obj, dict):
            return customer_obj
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": customer_obj.id},
        }
        return response, 201


@customer.route("/<int:customer_id>")
class GetCustomer(Resource):

    @staticmethod
    def get(customer_id: int):
        customer_obj = CustomerAction()
        customer_obj = customer_obj.get_customer(customer_id)
        if isinstance(customer_obj, dict):
            return customer_obj, 400
        return customer_obj


@customer.route("/update/<int:customer_id>")
class UpdateCustomer(Resource):

    @staticmethod
    @customer.expect(customer_model, validate=False)
    def put(customer_id: int):
        data = request.get_json()
        customer_obj = CustomerAction()
        customer_obj = customer_obj.update_customer(customer_id, data)
        if isinstance(customer_obj, dict):
            return customer_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": customer_obj.id},
        }
        return response, 200


@customer.route("/delete/<int:customer_id>")
class DeleteCustomer(Resource):

    @staticmethod
    def delete(customer_id: int):

        customer_obj = CustomerAction()
        customer_obj = customer_obj.delete_customer(customer_id)
        if isinstance(customer_obj, dict):
            return customer_obj, 400

        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204

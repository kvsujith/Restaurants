from flask import request
from flask_restx import Resource
from api.namespaces import invoice
from api.models.invoice import invoice_model
from actions.invoice import Invoice as InvoiceAction


@invoice.route("")
class Invoice(Resource):

    @staticmethod
    def get():
        invoice_obj = InvoiceAction()
        invoice_obj = invoice_obj.get_invoices()
        if isinstance(invoice_obj, dict):
            return invoice_obj, 400
        return invoice_obj

    @staticmethod
    @invoice.expect(invoice_model, validate=True)
    def post():
        data = request.get_json()
        invoice_obj = InvoiceAction()
        invoice_obj = invoice_obj.create_invoice(data)
        if isinstance(invoice_obj, (dict, list)):
            return invoice_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": invoice_obj.id},
        }
        return response, 201


@invoice.route("/<int:invoice_id>")
class GetInvoice(Resource):

    @staticmethod
    def get(invoice_id: int):
        invoice_obj = InvoiceAction()
        invoice_obj = invoice_obj.get_invoice(invoice_id)
        if isinstance(invoice_obj, dict):
            return invoice_obj, 400
        return invoice_obj


@invoice.route("/update/<int:invoice_id>")
class UpdateInvoice(Resource):

    @staticmethod
    @invoice.expect(invoice_model, validate=False)
    def put(invoice_id: int):
        data = request.get_json()
        invoice_obj = InvoiceAction()
        invoice_obj = invoice_obj.update_invoice(invoice_id, data)
        if isinstance(invoice_obj, (dict, list)):
            return invoice_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {"id": invoice_obj.id},
        }
        return response, 200


@invoice.route("/delete/<int:invoice_id>")
class DeleteInvoice(Resource):

    @staticmethod
    def delete(invoice_id: int):
        invoice_obj = InvoiceAction().delete_invoice(invoice_id)
        if isinstance(invoice_obj, dict):
            return invoice_obj, 400
        response = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_DELETED",
        }
        return response, 204

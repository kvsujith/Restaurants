from flask import g
from data.invoice import Invoice as InvoiceData
from db.enums.enum import PaymentStatus


class Invoice:
    """
    Action class for Customer
    """

    @staticmethod
    def get_invoice(invoice_id: int):
        return InvoiceData().get_invoice(invoice_id)

    @staticmethod
    def get_invoices():
        invoice_obj = InvoiceData()
        invoice_obj = invoice_obj.get_invoices()
        if isinstance(invoice_obj, dict):
            return invoice_obj, 400
        return invoice_obj

    @staticmethod
    def create_invoice(data: dict):
        try:
            data.update({"created_by": g.user_id})

            invoice_obj = InvoiceData()
            PaymentStatus(data["payment_status"])
            errors = invoice_obj.validate_data(data)
            if errors:
                return errors
            return invoice_obj.create_invoice(data)
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update_invoice(invoice_id: int, data: dict):
        try:
            if not data:
                return {"error": "Please provide at least one field for update."}
            data.update({
                "modified_by": g.user_id
            })

            invoice_obj = InvoiceData()
            if data.get("payment_status"):
                PaymentStatus(data["payment_status"])
            errors = invoice_obj.validate_data(data)
            if errors:
                return errors
            return invoice_obj.update_invoice(invoice_id, data)

        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete_invoice(invoice_id: int):
        return InvoiceData().delete_invoice(invoice_id)

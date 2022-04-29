from data import SessionData
from data.orders import Orders
from db.enums.enum import PaymentStatus
from db.entity.order import Order as OrderDB
from db.entity.invoice import Invoice as InvoiceDB
from db.entity.customer import Customer as CustomerDB
from db.entity.customer_invoice import CustomerInvoice
from db.entity.restaurant import Restaurant as RestaurantDB



class Invoice(SessionData):

    def get_invoice(self, invoice_id: int):
        try:
            invoice_obj = self.session.query(InvoiceDB, CustomerInvoice).join(CustomerInvoice) \
                .filter(InvoiceDB.id == invoice_id).first()
            if invoice_obj is None:
                raise ValueError("No resource found")
            invoice, cust_invoice = invoice_obj
            return {
                "id": invoice.id,
                "payment_status": invoice.status.name,
                "created_at": invoice.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": invoice.modified_at.strftime("%Y-%m-%d %H:%M:%S") if invoice.modified_at else None,
                "created_by": invoice.created_by,
                "modified_by": invoice.modified_by,
                "restaurant_id": invoice.restaurant_id,
                "restaurant_name": Orders().get_restaurant_name(invoice.restaurant_id),
                "order_id": invoice.order_id,
                "order_items": Orders().get_dish_items(invoice.order_id),
                "customer_id": cust_invoice.customer_id,
                "customer_name": self.get_customer_name(cust_invoice.customer_id),
            }
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def get_customer_name(self, customer_id: int):
        name = self.session.query(CustomerDB).get(customer_id)
        return name.name

    def get_invoices(self):
        try:
            invoice_obj = self.session.query(InvoiceDB, CustomerInvoice).join(CustomerInvoice).all()
            return [{
                "id": invoice.id,
                "payment_status": invoice.status.name,
                "created_at": invoice.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": invoice.modified_at.strftime("%Y-%m-%d %H:%M:%S") if invoice.modified_at else None,
                "created_by": invoice.created_by,
                "modified_by": invoice.modified_by,
                "restaurant_id": invoice.restaurant_id,
                "restaurant_name": Orders().get_restaurant_name(invoice.restaurant_id),
                "order_id": invoice.order_id,
                "order_items": Orders().get_dish_items(invoice.order_id),
                "customer_id": cust_invoice.customer_id,
                "customer_name": self.get_customer_name(cust_invoice.customer_id),
            } for invoice, cust_invoice in invoice_obj]
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def validate_data(self, data: dict):
        errors = []
        if data.get("customer_id"):
            if self.session.query(CustomerDB).get(data["customer_id"]) is None:
                errors.append({"customer_id": f"Invalid customer id : '{data['customer_id']}'."})

        if data.get("order_id"):
            if self.session.query(OrderDB).get(data["order_id"]) is None:
                errors.append({"order_id": f"Invalid Order id : '{data['order_id']}'."})

        if data.get("restaurant_id"):
            if self.session.query(RestaurantDB).get(data["restaurant_id"]) is None:
                errors.append({"restaurant_id": f"Invalid Restaurant id : '{data['restaurant_id']}'."})

        if data.get("restaurant_id") and data.get("order_id"):
            if self.session.query(OrderDB).filter_by(id=data["order_id"], restaurant_id=data["restaurant_id"]).first() is None:
                errors.append({"mismatch": f"Given Order id : '{data['order_id']}' is not tagged to given Restaurant "
                                           f"id '{data['restaurant_id']}'."})

        return errors

    def create_invoice(self, data: dict):
        try:
            customer_id = data["customer_id"]
            data.pop("customer_id")
            invoice_obj = InvoiceDB(
                status=PaymentStatus(data["payment_status"]).name,
                restaurant_id=data["restaurant_id"],
                order_id=data["order_id"],
                created_by=data["created_by"]
            )
            self.session.add(invoice_obj)
            self.session.commit()
            self.session.refresh(invoice_obj)
            customer_invoice = CustomerInvoice(customer_id=customer_id, invoice_id=invoice_obj.id)
            self.session.add(customer_invoice)
            self.session.commit()
            self.session.refresh(invoice_obj)
            return invoice_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def update_invoice(self, invoice_id: int, data: dict):
        try:
            invoice_obj = self.session.query(InvoiceDB).get(invoice_id)
            if invoice_obj is None:
                raise ValueError("No resource found")

            if data.get("restaurant_id"):
                if self.session.query(OrderDB).filter_by(id=invoice_obj.order_id, restaurant_id=data["restaurant_id"]).first() is None:
                    raise ValueError(f"Given restaurant_id {data['restaurant_id']} is not tagged to existing order id '{invoice_obj.order_id}'")
            if data.get("order_id"):
                if self.session.query(OrderDB).filter_by(id=data['order_id'], restaurant_id=invoice_obj.restaurant_id).first() is None:
                    raise ValueError(f"Given restaurant_id {invoice_obj.restaurant_id} is not tagged to existing "
                                     f"order id '{data['order_id']}'")
            try:
                customer_id = data["customer_id"]

                cust_invoice = self.session.query(CustomerInvoice).filter(CustomerInvoice.invoice_id==invoice_obj.id).first()
                cust_invoice.customer_id = customer_id
                self.session.commit()
                self.session.refresh(cust_invoice)

                data.pop("customer_id")
            except KeyError:
                pass
            for key, value in data.items():
                setattr(invoice_obj, key, value)
            self.session.commit()
            self.session.refresh(invoice_obj)
            return invoice_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def delete_invoice(self, invoice_id: int):
        try:
            invoice_obj = self.session.query(InvoiceDB).get(invoice_id)
            if invoice_obj is None:
                raise ValueError("No resource found")
            cust_invoice = self.session.query(CustomerInvoice).filter(CustomerInvoice.invoice_id == invoice_obj.id).first()
            self.session.delete(cust_invoice)
            self.session.delete(invoice_obj)
            self.session.commit()
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
        else:
            return True

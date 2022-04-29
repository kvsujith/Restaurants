from flask import g
from data.customer import Customer as customerData


class Customer:
    """
    Action class for Customer
    """

    @staticmethod
    def get_customer(customer_id: int):
        return customerData().get_customer(customer_id)

    @staticmethod
    def get_customers():
        return customerData().get_customers()

    @staticmethod
    def create_customer(data: dict):
        try:
            data.update({
                "created_by": g.user_id
            })
            customer_obj = customerData()
            customer_obj.validate_customer_phone(data["phone"])
            return customer_obj.create_customer(data)
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update_customer(customer_id: int, data: dict):
        try:
            if not data:
                return {"error": "Please provide at least one field for update."}
            data.update({
                "modified_by": g.user_id
            })
            customer_obj = customerData()
            if data.get("phone"):
                customer_obj.validate_customer_phone(data["phone"], customer_id)
            return customer_obj.update_customer(customer_id, data)

        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete_customer(customer_id: int):
        return customerData().delete_customer(customer_id)

from data import SessionData
from db.entity.customer import Customer as CustomerDB


class Customer(SessionData):

    def validate_customer_id(self, customer_id: int):
        customer_obj = self.session.query(CustomerDB).get(customer_id)
        if customer_obj is None:
            raise ValueError("No resource found")
        return customer_obj

    def validate_customer_phone(self, phone: str, customer_id=None):
        if customer_id is None:
            if self.session.query(CustomerDB).filter_by(phone=phone).first():
                raise ValueError("This contact is already registered.")
        else:
            if self.session.query(CustomerDB).filter(CustomerDB.phone == phone, CustomerDB.id != customer_id).first():
                raise ValueError("This contact is already registered to other user.")

    def get_customer(self, customer_id: int):
        try:
            customer_obj = self.validate_customer_id(customer_id)
            return {
                "id": customer_obj.id,
                "name": customer_obj.name,
                "phone": customer_obj.phone,
                "created_at": customer_obj.created_at.strftime(
                    "%Y-%m-%d %H:%M:%S"),
                "modified_at": customer_obj.modified_at.strftime(
                    "%Y-%m-%d %H:%M:%S") if customer_obj.modified_at else None,
                "created_by": customer_obj.created_by,
                "modified_by": customer_obj.modified_by,
            }
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def get_customers(self):
        try:
            customers = self.session.query(CustomerDB).all()
            return [{
                "id": customer.id,
                "name": customer.name,
                "phone": customer.phone,
                "created_at": customer.created_at.strftime(
                    "%Y-%m-%d %H:%M:%S"),
                "modified_at": customer.modified_at.strftime(
                    "%Y-%m-%d %H:%M:%S") if customer.modified_at else None,
                "created_by": customer.created_by,
                "modified_by": customer.modified_by,
            } for customer in customers]
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def create_customer(self, data: dict):
        try:
            customer_obj = CustomerDB(**data)
            self.session.add(customer_obj)
            self.session.commit()
            self.session.refresh(customer_obj)
            return customer_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def update_customer(self, customer_id: int, data: dict):
        try:
            customer_obj = self.validate_customer_id(customer_id)
            for key, value in data.items():
                setattr(customer_obj, key, value)
                self.session.commit()
                self.session.refresh(customer_obj)
            return customer_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def delete_customer(self, customer_id: int):
        try:
            customer_obj = self.validate_customer_id(customer_id)
            self.session.delete(customer_obj)
            self.session.commit()
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
        else:
            return True

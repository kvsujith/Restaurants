from data import SessionData
from db.entity.restaurant import Restaurant as RestaurantDB
from db.entity.dining_table import DiningTable as DiningTableDB


class DiningTable(SessionData):

    def get_dining_table(self, dining_table_id: int):
        try:
            dining_table = self.session.query(DiningTableDB, RestaurantDB).join(RestaurantDB).filter(
                DiningTableDB.id == dining_table_id).first()
            if dining_table is None:
                raise ValueError("No resource found")
            return dining_table
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def get_dining_tables(self):
        try:
            dining_tables = self.session.query(DiningTableDB, RestaurantDB).join(RestaurantDB).all()
            if dining_tables is None:
                raise ValueError("No resource found")
            return dining_tables
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def validate_restaurant(self, restaurant_id: int):
        return self.session.query(RestaurantDB).get(restaurant_id)

    def validate_table_no(self, table_no: int, restaurant_id: int):
        return self.session.query(DiningTableDB).filter_by(table_no=table_no, restaurant_id=restaurant_id).first()

    def validate_table_no_for_update(self, table_no: int, restaurant_id: int, dining_table_id: int):
        return self.session.query(DiningTableDB).filter(DiningTableDB.table_no == table_no,
                                                        DiningTableDB.restaurant_id == restaurant_id,
                                                        DiningTableDB.id != dining_table_id).first()

    def create_dining_table(self, data: dict):
        try:
            dining_table = DiningTableDB(**data)
            self.session.add(dining_table)
            self.session.commit()
            self.session.refresh(dining_table)
            return dining_table
        except Exception as e:
            return {"error": str(e)}

    def update_dining_table(self, dining_table_id: int, data: dict):
        try:
            dining_obj = self.session.query(DiningTableDB).get(dining_table_id)
            if dining_obj is None:
                raise ValueError("No resource found")

            if self.validate_restaurant(data["restaurant_id"]) is None:
                raise ValueError(f"Invalid restaurant_id '{data['restaurant_id']}' ")
            if self.validate_table_no_for_update(data["table_no"], data["restaurant_id"], dining_obj.id):
                raise ValueError(f"Duplicate table no.  Table no : '{data['table_no']}' is already assigned. ")

            for key, value in data.items():
                setattr(dining_obj, key, value)
            self.session.commit()
            self.session.refresh(dining_obj)
            return dining_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def delete_dining_table(self, dining_table_id):
        try:
            dining_obj = self.session.query(DiningTableDB).get(dining_table_id)
            if dining_obj is None:
                raise ValueError("No resource found")
            self.session.delete(dining_obj)
            self.session.commit()
            return True
        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

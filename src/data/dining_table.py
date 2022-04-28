from data import SessionData
from db.entity.restaurant import Restaurant as RestaurantDB
from db.entity.dining_table import DiningTable as DiningTableDB


class DiningTable(SessionData):

    def get_dining_table(self, dining_table_id: int):
        try:
            dining_table = self.session.query(DiningTableDB, RestaurantDB).join(RestaurantDB).filter(
                DiningTableDB.id == dining_table_id).all()
            if dining_table is None:
                raise ValueError("No resource found")
            return dining_table
        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

    def create_dining_table(self, data: dict):
        try:
            return []
        except Exception as e:
            return {"error": str(e)}

    def update_dining_table(self, dining_table_id: int, data: dict):
        try:
            return
        except ValueError:
            return {
                "error": "No resource found"
            }

    def delete_dining_table(self, dining_table_id):
        try:
            return True

        except ValueError as e:
            return {"error": str(e)}

        except Exception as e:
            return {"error": str(e)}

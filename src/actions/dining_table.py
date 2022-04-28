from flask import g
from data.dining_table import DiningTable as DiningTableData


class DiningTable:
    """
    Action class for DiningTable
    """

    @staticmethod
    def get_dining_table(dining_table_id: int):
        data = DiningTableData().get_dining_table(dining_table_id)
        if isinstance(data, dict):
            return data
        dining_table, restaurant = data
        return {
            "id": dining_table.id,
            "table_no": dining_table.table_no,
            "description": dining_table.description,
            "restaurant_id": restaurant.name,
            "occupied": dining_table.occupied,
            "created_at": dining_table.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "modified_at": dining_table.modified_at.strftime("%Y-%m-%d %H:%M:%S") if dining_table.modified_at else None,
            "created_by": dining_table.created_by,
            "modified_by": dining_table.modified_by,
        }

    @staticmethod
    def get_dining_tables():
        dining_tables = DiningTableData().get_dining_tables()
        return[
            {
                "id": dining_table.id,
                "table_no": dining_table.table_no,
                "description": dining_table.description,
                "restaurant_id": restaurant.name,
                "occupied": dining_table.occupied,
                "created_at": dining_table.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_at": dining_table.modified_at.strftime(
                    "%Y-%m-%d %H:%M:%S") if dining_table.modified_at else None,
                "created_by": dining_table.created_by,
                "modified_by": dining_table.modified_by,
            } for dining_table, restaurant in  dining_tables   ]

    @staticmethod
    def create_dining_table(data: dict):
        try:
            data.update({
                "created_by": g.user_id
            })
            dining_table = DiningTableData()
            if dining_table.validate_restaurant(data["restaurant_id"]) is None:
                raise ValueError(f"Invalid restaurant_id '{data['restaurant_id']}' ")

            if dining_table.validate_table_no(data["table_no"], data["restaurant_id"]):
                raise ValueError(f"Duplicate table_no .Table No : '{data['table_no']}' is already tagged.")

            dining_table = dining_table.create_dining_table(data)
            return dining_table
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update_dining_table(dining_table_id: int, data: dict):
        if not data:
            return {"error": "Please provide at least one field for updation"}
        data.update({
            "modified_by": g.user_id,
        })
        return DiningTableData().update_dining_table(dining_table_id, data)

    @staticmethod
    def delete_dining_table(dining_table_id: int):
        return DiningTableData().delete_dining_table(dining_table_id)

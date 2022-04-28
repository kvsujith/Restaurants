from flask import g
from data.dining_table import DiningTable as DiningTableData


class DiningTable:
    """
    Action class for DiningTable
    """

    @staticmethod
    def get_dining_table(dining_table_id: int):
        dining_table, restaurant = DiningTableData().get_dining_table(dining_table_id)
        return {

        }

    @staticmethod
    def get_dining_tables():
        return DiningTableData()

    @staticmethod
    def create_dish(data: dict):
        data.update({
            "created_by": g.user_id
        })

        return []

    @staticmethod
    def update_dish(dining_table_id: int, data: dict):
        if not data:
            return {"error": "Please provide at least one field for updation"}
        data.update({
            "modified_by": g.user_id,
        })

    @staticmethod
    def delete_dish(dining_table_id: int):
        return []

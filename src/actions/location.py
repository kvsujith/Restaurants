"""actions file for Tag"""
from flask import g
from data.location import Location as LocationData


class Location:
    """
    Action class for Location
    """

    @staticmethod
    def get_location(location_id: int):
        location_data = LocationData().get_location(location_id)
        if isinstance(location_data, dict):
            return location_data
        location_data = {
            "id": location_data.id,
            "name": location_data.name,
            "type": location_data.type.value,
            "created_by": location_data.created_by,
            "modified_by": location_data.modified_by,
            "created_at": location_data.created_at.strftime("%Y-%m-%dT%H:%M:%S") if location_data.created_at else None,
            "modified_at": location_data.modified_at.strftime(
                "%Y-%m-%dT%H:%M:%S") if location_data.modified_at else None,
        }
        return location_data

    @staticmethod
    def get_locations():
        location_data = LocationData().get_locations()
        location_data = [
            {
                "id": location.id,
                "name": location.name,
                "type": location.type.value,
                "created_by": location.created_by,
                "modified_by": location.modified_by,
                "created_at": location.created_at.strftime(
                    "%Y-%m-%dT%H:%M:%S") if location.created_at else None,
                "modified_at": location.modified_at.strftime(
                    "%Y-%m-%dT%H:%M:%S") if location.modified_at else None,
            } for location in location_data
        ]
        return location_data

    @staticmethod
    def create_location(data: dict):
        if data["name"].strip() == "":
            return {"name": "name field shouldn't left to be blank"}
        data.update({
            "created_by": g.user_id
        })
        location_data = LocationData()
        location_data = location_data.create_location(data)
        return location_data

    @staticmethod
    def update_location(location_id: int, data: dict):
        if data["name"].strip() == "":
            return {"name": "name field shouldn't left to be blank"}
        data.update({
            "modified_by": g.user_id
        })
        return LocationData().update_location(location_id, data)

    @staticmethod
    def delete_location(location_id: int):
        return LocationData().delete_location(location_id)

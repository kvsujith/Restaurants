"""data file for Location data"""
from data import SessionData
from db.entity.location import Location as LocationDB


class Location(SessionData):
    """
    Location data class with functions for creating a location,listing location, list a location_id based on id,
    delete a location based on location id and update location based on location id
    """

    def __init__(self):
        super(Location, self).__init__()

    def get_location(self, location_id):
        try:
            location_obj = self.session.query(LocationDB).get(location_id)
            if location_obj is None:
                raise ValueError("ro resource found")
            return location_obj
        except ValueError as e:
            return {"error": str(e)}

    def get_locations(self):
        return self.session.query(LocationDB).all()

    def create_location(self, data: dict):
        location_obj = LocationDB(name=data["name"], created_by=data["created_by"])
        self.session.add(location_obj)
        self.session.commit()
        self.session.refresh(location_obj)
        return location_obj

    def update_location(self, location_id: int, data: dict):
        try:
            location_obj = self.session.query(LocationDB).get(location_id)
            if location_obj is None:
                raise ValueError("No resource found")
            for key, value in data.items():
                setattr(location_obj, key, value)
            self.session.commit()
            self.session.refresh(location_obj)
            return location_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def delete_location(self, location_id: int):
        try:
            location_obj = self.session.query(LocationDB).get(location_id)
            if location_obj is None:
                raise ValueError("No resource found")
            self.session.delete(location_obj)
            self.session.commit()
            return True
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

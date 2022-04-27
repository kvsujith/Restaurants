from data import SessionData, engine
from db.entity.tag import Tag as TagDB
from db.entity.location import Location as LocationDB
from db.entity.restaurant import Restaurant as RestaurantDB
from db.entity.restaurant_tag import RestaurantTag as RestaurantTagDB
from db.entity.restaurant_location import RestaurantLocation as RestaurantLocationDB
from db.enums.enum import TagType


class Restaurant(SessionData):

    def get_restaurant_locations(self, restaurant_id: int):
        """
        return the locations available for the given restaurant_id using joins
        :param restaurant_id:
        :return:
        """
        return [location.name for location in self.session.query(LocationDB.name).join(RestaurantLocationDB).filter(
            RestaurantLocationDB.restaurant_id == restaurant_id).all()]

    def get_restaurant_tags(self, restaurant_id: int):
        return [tag.name for tag in self.session.query(TagDB.name).join(RestaurantTagDB).filter(
            RestaurantTagDB.restaurant_id == restaurant_id).all()]

    def get_restaurant(self, restaurant_id):
        try:
            restaurant_obj = self.session.query(RestaurantDB).get(restaurant_id)
            if restaurant_obj is None:
                raise ValueError("No resource found")
            return restaurant_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def get_restaurants(self):
        return [{
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "locations": self.get_restaurant_locations(restaurant.id),
            "tags": self.get_restaurant_tags(restaurant.id),
            "created_at": restaurant.created_at.strftime("%Y-%m-%d %H:%M:%S") if restaurant.created_at else None,
            "modified_at": restaurant.modified_at.strftime("%Y-%m-%d %H:%M:%S") if restaurant.modified_at else None,
            "created_by": restaurant.created_by,
            "modified_by": restaurant.modified_by,
        } for restaurant in self.session.query(RestaurantDB).all()]

    def validate_tags(self, tags: list):
        error_tags = []
        for tag in tags:
            if self.session.query(TagDB).filter(TagDB.type == TagType(1).name, TagDB.id == tag).first() is None:
                error_tags.append({"error": f"Invalid restaurant tag id '{tag}'."})
        return error_tags

    def validate_locations(self, locations: list):
        error_tags = []
        for location in locations:
            if self.session.query(LocationDB).get(location) is None:
                error_tags.append({"error": f"Invalid location id '{location}'."})
        return error_tags

    def create_restaurant(self, data):
        restaurant_obj = RestaurantDB(name=data["name"], description=data["description"], created_by=data['created_by'])
        self.session.add(restaurant_obj)
        self.session.commit()
        self.session.refresh(restaurant_obj)
        restaurant_tags = [RestaurantTagDB(restaurant_id=restaurant_obj.id, tag_id=tag) for tag in data["tags"]]
        restaurant_locations = [RestaurantLocationDB(restaurant_id=restaurant_obj.id, location_id=location) for location
                                in
                                data["locations"]]
        restaurant_locations.extend(restaurant_tags)
        self.session.add_all(restaurant_locations)
        self.session.commit()
        self.session.refresh(restaurant_obj)
        return restaurant_obj

    def update_restaurant(self, restaurant_id, data):
        try:
            restaurant_obj = self.session.query(RestaurantDB).get(restaurant_id)
            if restaurant_obj is None:
                raise ValueError("No resource found")

            for location in self.session.query(RestaurantLocationDB).filter_by(restaurant_id=restaurant_obj.id):
                self.session.delete(location)
            self.session.commit()

            for tag in self.session.query(RestaurantTagDB).filter_by(restaurant_id=restaurant_obj.id):
                self.session.delete(tag)
            self.session.commit()

            restaurant_tags = [RestaurantTagDB(restaurant_id=restaurant_obj.id, tag_id=tag) for tag in data["tags"]]
            restaurant_locations = [RestaurantLocationDB(restaurant_id=restaurant_obj.id, location_id=location) for
                                    location
                                    in
                                    data["locations"]]
            restaurant_locations.extend(restaurant_tags)
            self.session.add_all(restaurant_locations)
            self.session.commit()

            data.pop("tags")
            data.pop("locations")

            for key, value in data.items():
                setattr(restaurant_obj, key, value)
            self.session.commit()
            self.session.refresh(restaurant_obj)
            return restaurant_obj
        except ValueError:
            return {
                "error": "No resource found"
            }

    def delete_restaurant(self, restaurant_id):
        try:
            restaurant_obj = self.session.query(RestaurantDB).get(restaurant_id)
            if restaurant_obj is None:
                raise ValueError("No resource found")
            for location in self.session.query(RestaurantLocationDB).filter_by(restaurant_id=restaurant_obj.id):
                self.session.delete(location)
            self.session.commit()

            for tag in self.session.query(RestaurantTagDB).filter_by(restaurant_id=restaurant_obj.id):
                self.session.delete(tag)
            self.session.commit()
            self.session.delete(restaurant_obj)
            self.session.commit()
            return True
        except ValueError:
            return False

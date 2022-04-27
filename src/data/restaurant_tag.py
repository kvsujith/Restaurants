from data import SessionData
from db.entity.tag import Tag as TagDB
from db.entity.restaurant import Restaurant as RestaurantDB
from db.entity.restaurant_tag import RestaurantTag as RestaurantTagDB


class RestaurantTag(SessionData):

    def get_data(self):
        return self.session.query(RestaurantTagDB).all()

    def create_restaurant_tag(self, data):
        try:

            if self.session.query(RestaurantDB).get(data["restaurant_id"]) is None:
                raise ValueError("No restaurant found")
            if self.session.query(TagDB).get(data["tag_id"]) is None:
                raise ValueError("No Tag found")
            restaurant_tag = RestaurantTagDB(**data)
            self.session.add(restaurant_tag)
            self.session.commit()
            self.session.refresh(restaurant_tag)
            return restaurant_tag
        except ValueError as e:
            return {
                "error": str(e)
            }

    def update_restaurant_tag(self, restaurant_tag_id, data):
        try:
            if self.session.query(RestaurantDB).get(data["restaurant_id"]) is None:
                raise ValueError("No restaurant found")
            if self.session.query(TagDB).get(data["tag_id"]) is None:
                raise ValueError("No Tag found")
            restaurant_tag_db = self.session.query(RestaurantTagDB).get(restaurant_tag_id)
            if restaurant_tag_db is None:
                raise ValueError("No resource  found")
            for key, value in data.items():
                setattr(restaurant_tag_db, key, value)
            self.session.commit()
            self.session.refresh(restaurant_tag_db)
            return restaurant_tag_db
        except ValueError as e:
            return {
                "error": str(e)
            }

    def delete_restaurant_tag(self, restaurant_tag_id):
        try:
            restaurant_tag_obj = self.session.query(RestaurantTagDB).get(restaurant_tag_id)
            if restaurant_tag_obj is None:
                raise ValueError("No resource found")
            self.session.delete(restaurant_tag_obj)
            self.session.commit()
            return True
        except ValueError as e:
            return {
                "error": str(e)
            }

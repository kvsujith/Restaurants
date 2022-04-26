from data import SessionData
from db.entity.restaurant import Restaurant as RestaurantDB


class Restaurant(SessionData):

    def get_data(self):
        return self.session.query(RestaurantDB).all()

    def create_restaurant(self, data):
        restaurant_obj = RestaurantDB(**data)
        self.session.add(restaurant_obj)
        self.session.commit()
        self.session.refresh(restaurant_obj)
        return restaurant_obj

    def update_restaurant(self, restaurant_id, data):
        try:
            restaurant_obj = self.session.query(RestaurantDB).get(restaurant_id)
            if restaurant_obj is None:
                raise ValueError("No resource found")
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
            self.session.delete(restaurant_obj)
            self.session.commit()
            return True
        except ValueError:
            return False

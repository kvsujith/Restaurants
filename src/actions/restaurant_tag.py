"""actions file for Restaurant Tag"""
from data.restaurant_tag import RestaurantTag as RestaurantTagData


class RestaurantTag:

    @staticmethod
    def get_restaurant_tag_data():
        restaurant_tag_data = RestaurantTagData()
        restaurant_tag_data = restaurant_tag_data.get_data()
        restaurant_tag_data = [
            {"id": item.id, "restaurant_id": item.restaurant_id, "tag_id": item.tag_id} for item in restaurant_tag_data
        ]
        return restaurant_tag_data

    @staticmethod
    def create_restaurant_tag(data):
        restaurant_data = RestaurantTagData()
        restaurant_data = restaurant_data.create_restaurant_tag(data)
        return restaurant_data

    @staticmethod
    def update_restaurant_tag(restaurant_tag_id, data):
        restaurant_tag_data = RestaurantTagData()
        restaurant_tag_data = restaurant_tag_data.update_restaurant_tag(restaurant_tag_id, data)
        return restaurant_tag_data

    @staticmethod
    def delete_restaurant_tag(restaurant_tag_id):
        return RestaurantTagData().delete_restaurant_tag(restaurant_tag_id)

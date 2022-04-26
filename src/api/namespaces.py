from flask_restx import Namespace

tag = Namespace("tag", description="Tag API")
restaurant = Namespace("restaurant", description="Restaurant API")
restaurant_tag = Namespace("restaurant_tag", description="Restaurant Tag API")

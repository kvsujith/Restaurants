from flask_restx import Namespace

tag = Namespace("tag", description="Tag API")
restaurant = Namespace("restaurant", description="Restaurant API")
restaurant_tag = Namespace("restaurant_tag", description="Restaurant Tag API")
location = Namespace("location", description="Location API")
restaurant_location = Namespace("restaurant_location", description="Restaurant Location API")
dish = Namespace("dish", description="Dish API")
dining_table = Namespace("dining_table", description="Dining Table API")
orders = Namespace("orders", description="Order API")
customer = Namespace("customer", description="Customer API")
invoice = Namespace("invoice", description="Invoice API")


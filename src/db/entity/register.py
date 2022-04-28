from db.entity.customer import Customer
from db.entity.order import Order
from db.entity.dining_table import DiningTable
from db.entity.invoice import Invoice
from db.entity.customer_invoice import CustomerInvoice
from db.entity.dish import Dish
from db.entity.dish_tag import DishTag
from db.entity.location import Location
from db.entity.order_dish import OrderDish
from db.entity.restaurant_location import RestaurantLocation
from db.entity.restaurant_tag import RestaurantTag
from db.entity.tag import Tag
from data import Base, engine


def migrate():
    Base.metadata.create_all(engine)

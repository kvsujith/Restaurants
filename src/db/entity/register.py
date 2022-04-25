from data import Base, engine
from .customer import Customer
from .customer_invoice import CustomerInvoice
from .dining_table import DiningTable
from .dining_table_dish import DiningTableDish
from .dish import Dish
from .dish_tag import DishTag
from .invoice import Invoice
from .location import Location
from .order import Order
from .order_dish import OrderDish
from .restaurant import Restaurant
from .restaurant_location import RestaurantLocation
from .restaurant_tag import RestaurantTag


def migrate():
    Base.metadata.create_all(engine)

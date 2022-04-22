from .Customer import Customer
from .CustomerInvoice import CustomerInvoice
from .DiningTable import DiningTable
from .DiningTableDish import DiningTableDish
from .Dish import Dish
from .DishTag import DishTag
from .Invoice import Invoice
from .Location import Location
from .Order import Order
from .RestaurantTag import RestaurantTag
from .Restaurant import Restaurant
from .RestaurantLocation import RestaurantLocation
from .Tag import Tag

from data import Base, engine


def migrate():
    Base.metadata.create_all(engine)

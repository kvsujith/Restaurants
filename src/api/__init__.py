from api import endpoints
from flask_restx import Api
from flask import Blueprint
from .endpoints.tag import tag
from .endpoints.dish import dish
from .endpoints.location import location
from .endpoints.restaurant import restaurant
from .endpoints.dining_table import dining_table
from .endpoints.orders import orders
from .endpoints.customer import customer
from .endpoints.invoice import invoice

__endpoints__ = endpoints

api_blueprint = Blueprint("api", __name__)

api = Api(
    api_blueprint,
    title="Restaurant API",
    description="Restaurant API",
    version="1.0.0",
    prefix="/"
)

api.add_namespace(tag)
api.add_namespace(location)
api.add_namespace(restaurant)
api.add_namespace(dish)
api.add_namespace(dining_table)
api.add_namespace(orders)
api.add_namespace(customer)
api.add_namespace(invoice)


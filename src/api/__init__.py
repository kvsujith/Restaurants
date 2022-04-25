from flask import Blueprint
from flask_restx import Api

from api import endpoints
from .endpoints.tag import tag

__endpoints__ = endpoints

api_blueprint = Blueprint("api", __name__)

api = Api(
    api_blueprint,
    title="Restaurant API",
    description="Restaurant API",
    version="1.0.0",
    prefix="/tag_api"
)

api.add_namespace(tag)

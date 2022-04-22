from flask import Blueprint
from flask_restx import Api

from api import endpoints
# from namespaces import (namespaces)

__endpoints__ = endpoints

api_blueprint = Blueprint("api", __name__)

api = Api(
    api_blueprint,
    title="Restaurant API",
    description="Restaurant API",
    version="1.0.0",
)
# api.add_namespace(serve_minio)

from flask_restx import fields
from api.namespaces import restaurant

restaurant_model = restaurant.model(
    'Restaurant',
    {
        'name': fields.String(required=True),
        'description': fields.String(required=True),
        'locations': fields.List(fields.Integer(required=True),required=True),
        'tags': fields.List(fields.Integer(required=True), required=True),
    }
)

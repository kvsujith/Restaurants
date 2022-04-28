from flask_restx import fields
from api.namespaces import dish

dish_model = dish.model(
    'Dish',
    {
        'name': fields.String(required=True),
        'description': fields.String(required=True),
        'restaurant_id': fields.Integer(required=True),
        'availability': fields.Boolean(required=True),
        'tags': fields.List(fields.Integer(required=True), required=True),
    }
)

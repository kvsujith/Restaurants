from flask_restx import fields
from api.namespaces import orders

orders_model = orders.model(
    'Orders',
    {
        'order_type': fields.Integer(required=True),
        'dining_table_id': fields.Integer(required=False),
        'special_message': fields.String(required=True),
        'order_status': fields.Integer(required=True),
        'restaurant_id': fields.Integer(required=True),
        "dish_items": fields.List(fields.Integer(required=True), required=True)
    }
)

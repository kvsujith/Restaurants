from flask_restx import fields
from api.namespaces import dining_table

dining_table_model = dining_table.model(
    'Dining Table',
    {
        'table_no': fields.String(required=True),
        'description': fields.String(required=True),
        'restaurant_id': fields.Integer(required=True),
        'occupied': fields.Boolean(required=True),
    }
)

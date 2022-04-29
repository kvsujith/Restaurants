from flask_restx import fields
from api.namespaces import invoice

invoice_model = invoice.model(
    'Invoice',
    {
        'restaurant_id': fields.Integer(required=True),
        'order_id': fields.Integer(required=True),
        'customer_id': fields.Integer(required=True),
        'payment_status': fields.Integer(required=True)
    }
)

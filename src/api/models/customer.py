from flask_restx import fields
from api.namespaces import customer

customer_model = customer.model(
    'Customer',
    {
        'name': fields.String(max_length=50, min_length=3, required=True),
        'phone': fields.String(max_length=13, min_length=10, required=True),
    }
)

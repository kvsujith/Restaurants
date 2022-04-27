from flask_restx import fields
from api.namespaces import tag

restaurant_model = tag.model(
    'Restaurant',
    {
        'name': fields.String(required=True),
        'description': fields.String(required=True),
        'locations': fields.List(fields.Integer(required=True),required=True),
        'tags': fields.List(fields.Integer(required=True), required=True),
    }
)

restaurant_view = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'created_by': fields.String,
    'created_at': fields.DateTime,
    'modified_by': fields.String,
    'modified_at': fields.DateTime,
}

from flask_restx import fields
from api.namespaces import tag

restaurant_tag_model = tag.model(
    'Restaurant Tag',
    {
        'restaurant_id': fields.Integer(required=True),
        'tag_id': fields.Integer(required=True),
    }
)
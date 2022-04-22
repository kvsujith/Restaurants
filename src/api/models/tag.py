from flask_restx import fields
from api.namespaces import tag


a_tag = tag.model(
    'Tag',
    {
        'name': fields.String(required=True),
        'type': fields.Integer(required=True),

    }
)

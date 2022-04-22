"""endpoint for tag"""
from flask import request
from flask_restx import Resource

from actions.tag import Tag as TagAction
from api.models.tag import a_tag
from api.namespaces import tag


@tag.route("")
class Tag(Resource):
    """
    Shows a list of all Tags and lets you POST to add new tag
    """

    @staticmethod
    @tag.expect(a_tag, validate=True)
    def post():
        """
        Create new tag
        :return: tag ID
        Example::
        #Data
            {
          "name": "Project A",
          "type": 1
          }
        """
        action_obj = TagAction()
        data = request.get_json()
        user_id = request.headers.get("userid")
        user_name = request.headers.get("username")
        data["user_id"] = user_id
        data["user_name"] = user_name
        action_result = action_obj.create_tag(data)
        result = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": action_result,
        }
        return result, 201

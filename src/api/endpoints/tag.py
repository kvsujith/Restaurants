"""endpoint for tag"""
from flask import request
from flask_restx import Resource
from actions.tag import Tag as TagAction
from api.models.tag import a_tag
from api.namespaces import tag


@tag.route("")
class Tag(Resource):

    @staticmethod
    def get():
        try:
            result = TagAction.get_tags()
            return result
        except Exception as e:
            return {"error": str(e)}, 500

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
        action_obj = action_obj.create_tag(data)
        if isinstance(action_obj, dict):
            return action_obj, 400
        result = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": {"id": action_obj.id},
        }
        return result, 201


@tag.route("/<int:tag_id>")
class Tag(Resource):

    @staticmethod
    def get(tag_id):
        try:
            return TagAction.get_tag(tag_id)
        except Exception as e:
            return {"error": str(e)}, 500


@tag.route("/update/<int:token>")
class TagUpdate(Resource):

    @staticmethod
    @tag.expect(a_tag, validate=True)
    def put(token):
        data = request.get_json()
        tag_obj = TagAction()
        tag_obj = tag_obj.update_tag(token, data)
        if isinstance(tag_obj, dict):
            return tag_obj, 400
        result = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": {
                "id": tag_obj.id
            },
        }
        return result, 200


@tag.route("/delete/<int:token>")
class TagUpdate(Resource):

    @staticmethod
    def delete(token):
        action_obj = TagAction()
        res = action_obj.delete_tag(token)
        if isinstance(res, bool):
            result = {
                "status": "SUCCESS",
                "code": 0,
                "message": "MESSAGE_DELETED",
            }
            return result, 204
        else:
            return res, 400

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
        action_result = action_obj.create_tag(data)
        if action_result.get("error"):
            return action_result, 400
        result = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_CREATED",
            "result": action_result,
        }
        return result, 201


@tag.route("/update/<int:token>")
class TagUpdate(Resource):

    @staticmethod
    @tag.expect(a_tag, validate=True)
    def put(token):
        data = request.get_json()
        action_obj = TagAction()
        res = action_obj.update_tag(token, data)
        if res.get("error"):
            return res
        result = {
            "status": "SUCCESS",
            "code": 0,
            "message": "MESSAGE_UPDATED",
            "result": res,
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

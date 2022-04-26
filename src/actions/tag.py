"""actions file for Tag"""
from sqlalchemy import and_

from data import SessionData
from data.tag import TagData
from db.entity.tag import Tag as TagDB


class Tag:
    """
    Action class for Tag
    """

    def __init__(self, tag_id=None):
        self.tag_id = tag_id

    @staticmethod
    def get_tags():
        tags = TagData().get_data()
        res = [
            {"id": item.id, "name": item.name, "type": item.type.value} for item in tags
        ]
        return res

    @staticmethod
    def create_tag(data):
        """
        Create a new tag
        :param data: Data that needs to be passed for creating the tag (name and tag type)
        :return: created tag id
        Example::
        #Data
        {
        "name": "Project A",
        "type": 1
        }
        """
        if data["name"].strip() == "":
            return {
                "status": True,
                "message": "Tag name field cannot be null"
            }

        tag_obj = TagData()

        if tag_obj.tag_exists(data["name"]):
            return {
                "error": f"Tag name '{data['name']}' already exists. "
            }

        created_tag = tag_obj.create_tag(data)

        result = {"id": created_tag.id}
        return result

    @staticmethod
    def update_tag(token, data):

        if data["name"].strip() == "":
            return {
                "status": True,
                "message": "Tag name field cannot be null"
            }

        tag_obj = TagData()

        if tag_obj.tag_exists(data["name"]):
            return {
                "error": f"Tag name '{data['name']}' already exists. "
            }

        created_tag = tag_obj.update_tag(token, data)
        if isinstance(created_tag, dict):
            if created_tag.get("error"):
                return created_tag
        return {"id": created_tag.id}

    @staticmethod
    def delete_tag(_id):
        tag_obj = TagData()
        created_tag = tag_obj.delete_tag(_id)
        if isinstance(created_tag, dict):
            if created_tag.get("error"):
                return created_tag
        return True

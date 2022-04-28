"""actions file for Tag"""
import datetime

from flask import g

from data.tag import TagData


class Tag:
    """
    Action class for Tag
    """

    def __init__(self, tag_id=None):
        self.tag_id = tag_id

    @staticmethod
    def get_tags():
        tags = TagData().get_tags()
        res = [
            {"id": item.id, "name": item.name, "type": item.type.value,
             "created_by": item.created_by,
             "modified_by": item.modified_by,
             "created_at": item.created_at.strftime("%Y-%m-%dT %H:%M:%S") if item.created_at else None,
             "modified_at": item.modified_at.strftime("%Y-%m-%dT %H:%M:%S") if item.modified_at else None,
             } for item in tags
        ]
        return res

    @staticmethod
    def get_tag(tag_id):
        tag = TagData().get_tag(tag_id)
        if isinstance(tag, dict):
            return tag
        tags = {"id": tag.id, "name": tag.name, "type": tag.type.value,
                "created_by": tag.created_by,
                "modified_by": tag.modified_by,
                "created_at": tag.created_at.strftime("%Y-%m-%dT %H:%M:%S") if tag.created_at else None,
                "modified_at": tag.modified_at.strftime("%Y-%m-%dT %H:%M:%S") if tag.modified_at else None
                }

        return tags

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
        return created_tag

    @staticmethod
    def update_tag(tag_id, data):

        if data["name"].strip() == "":
            return {
                "error": "Tag name field cannot be null"
            }

        tag_obj = TagData()
        data.update({
            "modified_by": g.user_id,
            "modified_at": datetime.datetime.now(),
        })
        created_tag = tag_obj.update_tag(tag_id, data)
        return created_tag

    @staticmethod
    def delete_tag(_id):
        tag_obj = TagData()
        created_tag = tag_obj.delete_tag(_id)
        if isinstance(created_tag, dict):
            if created_tag.get("error"):
                return created_tag
        return True

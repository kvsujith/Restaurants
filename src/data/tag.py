"""data file for tag data"""
from sqlalchemy import and_

from data import SessionData
from db.enums.enum import TagType
from flask import g
from db.entity.tag import Tag

from utils.utils import get_indian_time


class TagData(SessionData):
    """
    Tag data class with functions for creating a tag,listing tags, list a tag based on id,
    delete a tag based on tag id and update tag based on tag id
    """

    def __init__(self, tag_id=None):
        super(TagData, self).__init__()
        self.tag_id = tag_id

    def tag_exists(self, name, token=None):

        if token is None:
            if self.session.query(Tag).filter(Tag.name == name).first():
                return True

            return False

        else:
            if SessionData().session.query(Tag).filter(and_(Tag.name == name, Tag.id != token)).first():
                return True

            return False

    def get_data(self):
        res = self.session.query(Tag).all()
        return res

    def create_tag(self, data: dict):
        """
        create a new tag
        :param data: Data that needs to be passed for creating the tag (name and tag type)
        :return: created tag
        Example::
         #Data
          {
          "name": "Tag Type,
          "type": 1
          }
        """
        tag_obj = Tag(name=data.get("name"), type=TagType(data.get("type")), created_by=g.user_id,
                      created_at=get_indian_time())

        self.session.add(tag_obj)
        self.session.commit()
        self.session.refresh(tag_obj)
        return tag_obj

    def update_tag(self, _id: int, data: dict):
        """

        :param _id: unique id of the object
        :param data: data for updating the tag object
        :return:
        """
        tag_obj = self.session.query(Tag).filter(Tag.id == _id).first()

        # set the right value of the TagType to the data
        data["type"] = TagType(data["type"])
        data["modified_by"] = g.user_id
        if tag_obj:

            for key, value in data.items():
                setattr(tag_obj, key, value)
            self.session.commit()
            return tag_obj
        else:
            return {"error": "No resource found"}

    def delete_tag(self, _id: int):
        """

        :param _id: unique id of the object
        :return: return true if deleted else False
        """
        tag_obj = self.session.query(Tag).get(_id)
        if tag_obj:
            self.session.delete(tag_obj)
            self.session.commit()
            return True
        else:
            return {"error": "No resource found"}

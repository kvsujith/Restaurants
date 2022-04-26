"""data file for tag data"""
from sqlalchemy import and_
from data import SessionData
from db.enums.enum import TagType
from flask import g
from db.entity.tag import Tag


class TagData(SessionData):
    """
    Tag data class with functions for creating a tag,listing tags, list a tag based on id,
    delete a tag based on tag id and update tag based on tag id
    """

    def __init__(self, tag_id=None):
        super(TagData, self).__init__()
        self.tag_id = tag_id

    def tag_exists(self, name, tag_id=None):
        if tag_id is None:
            if self.session.query(Tag).filter(Tag.name == name).first():
                return True
            else:
                return False
        else:
            if self.session.query(Tag).filter(and_(Tag.name == name, Tag.id != tag_id)).first():
                return True
            else:
                return False

    def get_tags(self):
        res = self.session.query(Tag).all()
        return res

    def get_tag(self, tag_id):
        try:
            tag_obj = self.session.query(Tag).get(tag_id)
            if tag_obj is None:
                raise ValueError("No resource found")
            return tag_obj
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

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
        try:
            tag_obj = Tag(name=data.get("name"), type=TagType(data.get("type")), created_by=g.user_id)

            self.session.add(tag_obj)
            self.session.commit()
            self.session.refresh(tag_obj)
            return tag_obj
        except Exception as e:
            return {"error": str(e)}

    def update_tag(self, _id: int, data: dict):
        """

        :param _id: unique id of the object
        :param data: data for updating the tag object
        :return:
        """
        try:
            tag_obj = self.session.query(Tag).filter(Tag.id == _id).first()

            # set the right value of the TagType to the data
            data["type"] = TagType(data["type"])
            data["modified_by"] = g.user_id
            if tag_obj:
                for key, value in data.items():
                    setattr(tag_obj, key, value)
                self.session.commit()
                self.session.refresh(tag_obj)
                return tag_obj
        except Exception as e:
            return {"error": str(e)}

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

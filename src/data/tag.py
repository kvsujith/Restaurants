"""data file for tag data"""
from data import SessionData
from db.entity.Tag import Tag
from db.enum import TagType


class TagData(SessionData):
    """
    Tag data class with functions for creating a tag,listing tags, list a tag based on id,
    delete a tag based on tag id and update tag based on tag id
    """

    def __init__(self, tag_id=None):
        super(TagData, self).__init__()
        self.tag_id = tag_id

    def create_tag(self, data):
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
        tag_obj = Tag(name=data.get("name"), type=TagType(data.get("type")), created_by=data.get("user_id"))
        self.session.add(tag_obj)
        self.session.commit()
        self.session.refresh(tag_obj)
        return tag_obj

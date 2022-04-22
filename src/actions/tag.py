"""actions file for Tag"""
from data.tag import TagData


class Tag:
    """
    Action class for Tag
    """

    def __init__(self, tag_id=None):
        self.tag_id = tag_id

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
        tag_obj = TagData()
        created_tag = tag_obj.create_tag(data)
        result = {"id": created_tag.id}
        return result

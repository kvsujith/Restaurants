"""actions file for Tag"""
from sqlalchemy import and_

from data import SessionData
from data.tag import TagData
from db.entity.tag import Tag as TagDB


class Tag:

    @staticmethod
    def create_restaurant(data):

        return {}

    @staticmethod
    def update_restaurant(token, data):

        return {}

    @staticmethod
    def delete_restaurant(_id):

        return True


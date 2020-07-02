#!/usr/bin/python3
"""
    this is a class model for ARBN proyect
    methods
    arg
"""


import time
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ this class is the base for all the classes
        atributes:
        id, created, udpdate
        methods:
        save, to_dict
    """

    def __init__(self, *args, **kwargs):
        """ inicialia class """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.update_at = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__> """
        return ('[{}] ({}) {}'.format(
            str(type(self).__name__), self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
             with the current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        list_dic = {}
        for key in self.__dict__:
            list_dic[key] = self.__dict__[key]
        list_dic['__class__'] = self.__class__.__name__
        list_dic['id'] = self.id
        list_dic['created_at'] = self.created_at.isoformat()
        list_dic['updated_at'] = self.updated_at.isoformat()
        return (list_dic)

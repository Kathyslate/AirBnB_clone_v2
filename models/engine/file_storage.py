#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review}

    def all(self, cls=None):
        """returns all"""
        all_return = {}

        if cls:
            if cls.__name__ in self.all_classes:
                for key, val in self.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        all_return.update({key: val})
        else:
            all_return = self.__objects

        return all_return

    def new(self, obj):
        """sets __object to given obj"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save as JSON file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """reload to JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """Reload JSON objects
        """
        return self.reload()

    def delete(self, obj=None):
        """delete obj if present
        """
        if obj:
            # format key from obj
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

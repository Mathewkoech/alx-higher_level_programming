#!/usr/bin/python3
import json

"""module for Base class"""


class Base:
    """Base class for managing id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs
        to file/serialize"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON str rep json_string/ deserialise"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                jsonfile = jsonfile.read()
                # convert json to list of dictionaries
                list_dicts = Base.from_json_string(jsonfile)
                # Create instances from dictionaries using the create method
                instances = [cls.create(**d) for d in list_dicts]
                return instances
        except FileNotFoundError:
            return []

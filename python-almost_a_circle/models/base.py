#!/usr/bin/python3
"""Defines the base of every shape of the project."""
import json


class Base:
    """Manages the id attribute of every shape.

    Holding that logic in one place avoids duplicating it, and the same
    bugs with it, in each shape that inherits this class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base with the given id.

        A missing id is replaced by the number of objects created so far.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list held by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a list of shapes to a file."""
        if list_objs is None:
            list_objs = []
        dictionaries = [shape.to_dictionary() for shape in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """Returns a shape whose attributes are set to the given values."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns the list of shapes stored in the file of this class."""
        try:
            with open("{}.json".format(cls.__name__),
                      encoding="utf-8") as a_file:
                dictionaries = cls.from_json_string(a_file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dictionary) for dictionary in dictionaries]

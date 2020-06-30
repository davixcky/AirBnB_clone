#!/usr/bin/python3
"""Module for handle storage"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

        key = '{}.{}'\
              .format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_data = {}
        for k, v in FileStorage.__objects.items():
            json_data[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_data, f)

    @staticmethod
    def create_object(info):
        """Create an instance from a dictionary"""
        class_obj = info['__class__']
        instance = '{}(**info)'.format(class_obj)
        return eval(instance)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        filename = FileStorage.__file_path

        if not os.path.exists(filename):
            return

        with open(filename) as f:
            dictionary_data = json.load(f)

        for k, v in dictionary_data.items():
            obj = FileStorage.create_object(v)
            FileStorage.__objects[k] = obj

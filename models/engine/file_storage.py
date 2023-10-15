#!/usr/bin/python3
"""File Storage Class Api"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """File Storage Class - acts as the storage engine
    Attributes:
        __file_path (str) : Json file to save storage objects
        __objects (dict) : Dict of all instantiated objects
    """

    __objects = {}
    __file_path = "file.json"

    def new(self, obj):
        "Add objects to storage using key as id and value as obj"
        obj_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_name}.{obj.id}"] = obj

    def all(self):
        "Returns all saved objects as dicts"
        return FileStorage.__objects

    def save(self):
        """Serialize objects as json and saves them"""
        all_objects = FileStorage.__objects
        file_path = FileStorage.__file_path
        to_save_dict = {obj: all_objects[obj].to_dict() for obj in all_objects.keys()}
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(to_save_dict, f)

    def reload(self):
        """Converts json back to dictionary"""
        try:
            with open(FileStorage.__file_path) as f:
                all_obj_dicts = json.load(f)
                for obj in all_obj_dicts.values():
                    cls_name = obj.pop("__class__")
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return

#!/usr/bin/python3
""" The Base Model Class for the project"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The Base Model for the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Init new Base Model
        Arguments:
            *args : positional arguments
            **kwargs : key word arguments
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updated_at matches the current timestamp or datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Get key & value pairs of the instance of Base Model
        using __class__ to get the name of the class as well
        """
        # make a copy of the class dict
        tmp_dict = self.__dict__.copy()
        tmp_dict["__class__"] = self.__class__.__name__
        tmp_dict["created_at"] = self.created_at.isoformat()
        tmp_dict["updated_at"] = self.updated_at.isoformat()
        return tmp_dict

    def __str__(self):
        """Returns str rep of the Base Model instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

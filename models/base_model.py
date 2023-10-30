#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel module"""


class BaseModel:
    """BaseModel class"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __str__(self):
        """str """
        return "[{}] ({}) {}".format(__name__, id, __dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict method"""
        to_dict = self.__dict__.copy()
        to_dict["__class__"] = __name__
        to_dict["created_at"] = to_dict["created_at"].isoformat()
        to_dict["updated_at"] = to_dict["updated_at"].isoformat()
        return to_dict

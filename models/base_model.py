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
        
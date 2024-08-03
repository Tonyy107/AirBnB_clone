#!/usr/bin/python3
from datetime import datetime


def save(self):
    """
    Updates the `updated_at` attribute with the current datetime.
    """
    self.updated_at = datetime.now()


def to_dict(self):
    """
    Converts the object to a dictionary representation.

    Returns:
        dict: A dictionary representation of the object.
    """
    self.updated_at = self.updated_at.strftime("%d/%m/%Y %H:%M:%S")
    self.created_at = self.created_at.strftime("%d/%m/%Y %H:%M:%S")
    return self.__class__.__dict__

#!/usr/bin/python3
from datetime import datetime
import uuid
"""basemodel module"""


class BaseModel():
    """
    Base class for all models in the AirBnB clone project.

    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The datetime when the model instance was created.
        updated_at (datetime): The datetime when the model instance was last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            id (str): The unique identifier for the object.
            created_at (datetime): The timestamp when the object was created.
            updated_at (datetime): The timestamp when the object was last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        The string representation includes the class name, the instance ID,
        and the dictionary representation of the instance attributes.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

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
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

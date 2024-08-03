#!/usr/bin/python3

from datetime import datetime
=======
"""basemodel module"""


class BaseModel():
    """
    Base class for all models in the AirBnB clone project.

    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The datetime when the model instance was created.
        updated_at (datetime): The datetime when the model instance was last updated.
    """

    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        The string representation includes the class name, the instance ID,
        and the dictionary representation of the instance attributes.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return f"[BaseModel] ({self.id}) {self.__dect__}"
      
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

#!/usr/bin/python3
from datetime import datetime

def save(self):
    self.updated_at = datetime.now()

def to_dict(self):
    self.updated_at = self.updated_at.strftime("%d/%m/%Y %H:%M:%S")
    self.created_at = self.created_at.strftime("%d/%m/%Y %H:%M:%S")
    return self.__class__.__dict__
#!/usr/bin/python3
from datetime import datetime

def save(self):
    self.updated_at = datetime.now()

def to_dict(self):
    dt_string = self.updated_at.strftime("%d/%m/%Y %H:%M:%S")
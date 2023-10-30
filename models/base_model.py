#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel module"""


class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at
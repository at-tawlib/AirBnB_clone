#!/usr/bin/python3
"""
module that contain the City class

Class:
    City : define City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""

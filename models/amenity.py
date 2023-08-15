#!/usr/bin/python3
<<<<<<< HEAD
""" Class Amenity """
=======
'''class inherent of BaseModel'''
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e
from models.base_model import BaseModel


class Amenity(BaseModel):
<<<<<<< HEAD
    """Amenity class that inherits BaseModel"""
    name = ""
=======
    '''class amenity'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e

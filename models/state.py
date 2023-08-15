#!/usr/bin/python3
<<<<<<< HEAD
""" Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
=======
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''class State'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e

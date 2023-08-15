#!/usr/bin/python3
<<<<<<< HEAD
""" Class Review """
=======
'''class inherent of BaseModel'''
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """ Review class that inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
=======
    '''class Review'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e

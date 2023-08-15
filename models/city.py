#!/usr/bin/python3
<<<<<<< HEAD
""" Class City """
=======
'''class inherent of BaseModel'''
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
    """ City class that inherits BaseModel """
    state_id = ""
    name = ""
=======
    '''class city'''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e

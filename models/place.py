#!/usr/bin/python3
<<<<<<< HEAD
""" Class Place """

=======
'''class inherent of Base Model'''
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """ Place class that inherits BaseModel """
=======
    '''class Place'''

>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
>>>>>>> 0673de5fbd77dc39d21712d93d9ec83183a33c2e

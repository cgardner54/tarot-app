""" Script to seed database"""
import os
import json
from random import choice, randint
#from datetime import datetime

import query
import model
import server

os.system('dropdb tarot')
os.system('createdb tarot')

model.connect_to_db(server.app)
model.db.create_all()

def create_seeds():
    """Create and return a new user."""

    card_death = Cards(card_name="Death", 
                        card_number="XIII", 
                        card_desc="Description of death",
                        card_reversed_desc="Reversed",
                        card_suit="Major_Arcana",
                        card_image="/static/death.jpg"
                        
      )

    db.session.add(card_death)
    db.session.commit()

    return card_death
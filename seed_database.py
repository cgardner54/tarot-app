""" Script to seed database"""
import os
import json
from random import choice, randint
#from datetime import datetime

import model
import server

os.system('dropdb tarot')
os.system('createdb tarot')

model.connect_to_db(server.app)
model.db.create_all()

def create_seeds():
    """Create and return a new user."""

    card_death = model.Card(card_name="Death", 
                        card_number="XIII", 
                        card_desc="Description of death",
                        card_reversed_desc="Reversed",
                        card_suit="Major_Arcana",
                        card_image="/static/death.jpg"
                        
      )

    card_empress = model.Card(card_name="Empress", 
                        card_number="III", 
                        card_desc="Description of Empress",
                        card_reversed_desc="Reversed Empress",
                        card_suit="Major_Arcana",
                        card_image="/static/empress.jpeg"
                        
      )

    deck_tarot = model.Deck(deck_name="Rider-Waite",
                      deck_type="Tarot",
                      number_of_cards=78
      )
    
    three_card_spread = model.Spread(spread_name="3 card",
                                      qty_cards_in_spread=3
      )
    
    amanda_user = model.User(user_name="Amanda2021")

    #test_reading = model.Readings(reading_id=1)

    model.db.session.add(card_empress)
    model.db.session.add(deck_tarot)
    model.db.session.commit()

    #model.db.session.add(test_reading)
    model.db.session.add(amanda_user)
    model.db.session.add(card_death)
    
    model.db.session.add(three_card_spread)
    model.db.session.commit()

    return card_death, card_empress, deck_tarot, three_card_spread #amanda_user


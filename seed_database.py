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

    card_death = model.Cards(card_name="Death", 
                        card_number="XIII", 
                        card_desc="Description of death",
                        card_reversed_desc="Reversed",
                        card_suit="Major_Arcana",
                        card_image="/static/death.jpg"
                        
      )

    card_empress = model.cards(card_name="Empress", 
                        card_number="III", 
                        card_desc="Description of Empress",
                        card_reversed_desc="Reversed Empress",
                        card_suit="Major_Arcana",
                        card_image="/static/empress.jpeg"
                        
      )

    deck_tarot = model.Decks(deck_name="Rider-Waite",
                      deck_type="Tarot",
                      number_of_cards=78
      )
    
    three_card_spread = model.Spreads(spread_id=1,
                                      spread_name="3 card",
                                      qty_cards_in_spreads=3
      )
    
    amanda_user = model.User(user_name="Amanda2021")

    test_reading = model.Readings(reading_id=1)

    model.db.session.add(test_reading, amanda_user, card_death, card_empress, deck_tarot, three_card_spread)
    model.db.session.commit()

    return card_death, card_empress, card_empress, deck_tarot, three_card_spread, amanda_user


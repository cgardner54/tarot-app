""" Script to seed database"""
import os
import json
from random import choice, randint
from model import db, connect_to_db, Card, Deck, Spread, User, Reading, CardReading
import server

os.system('dropdb tarot')
os.system('createdb tarot')

connect_to_db(server.app)
db.create_all()


"""Create and return a new user."""

card_death = Card(card_name="Death", 
                    card_number="XIII", 
                    card_desc="Description of death",
                    card_reversed_desc="Reversed",
                    card_suit="Major_Arcana",
                    card_image="/static/death.jpg"
                    
  )

card_empress = Card(card_name="Empress", 
                    card_number="III", 
                    card_desc="Description of Empress",
                    card_reversed_desc="Reversed Empress",
                    card_suit="Major_Arcana",
                    card_image="/static/empress.jpeg"
                    
  )

deck_tarot = Deck(deck_name="Rider-Waite",
                  deck_type="Tarot",
                  number_of_cards=78
  )

three_card_spread = Spread(spread_name="3 card",
                                  qty_cards_in_spread=3
  )

amanda_user = User(user_name="Amanda2021")

test_reading = Reading(reading_name="test")

card_reading1 = CardReading(card_id=card_death.card_id, reading_id=test_reading.reading_id)

db.session.add(card_empress)
db.session.add(deck_tarot)
db.session.commit()

db.session.add(test_reading)
db.session.add(amanda_user)
db.session.add(card_death)

db.session.add(three_card_spread)
db.session.add(card_reading1)
db.session.commit()



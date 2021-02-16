""" Script to seed database"""
import os
import json
from random import choice, randint
from model import db, Card, Deck, Spread, User, Reading, CardReading , connect_to_db 
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

card_priestess = Card(card_name="High Priestess", 
                    card_number="II", 
                    card_desc="Description of EmpHigh Priestess",
                    card_reversed_desc="Reversed Priestess",
                    card_suit="Major_Arcana",
                    card_image="/static/02_High_Priestess.jpg"
                    
  )
card_fool = Card(card_name="fool", 
                    card_number="II", 
                    card_desc="Description of the fool",
                    card_reversed_desc="Reversed fool",
                    card_suit="Major_Arcana",
                    card_image="/static/thefool.jpg"
                    
  )
card_moon = Card(card_name="the moon", 
                    card_number="II", 
                    card_desc="Description of the moon",
                    card_reversed_desc="Reversed moon",
                    card_suit="Major_Arcana",
                    card_image="/static/themoon.jpeg"
                    
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
db.session.add(card_priestess)
db.session.add(card_fool)
db.session.add(deck_tarot)
db.session.add(card_death)
db.session.add(card_moon)
db.session.commit()

db.session.add(test_reading)
db.session.add(amanda_user)


db.session.add(three_card_spread)
db.session.add(card_reading1)
db.session.commit()



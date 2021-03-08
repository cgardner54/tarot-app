""" Data Model for Tarot-app """
import os
import requests, random
from flask_sqlalchemy import SQLAlchemy
#from flask import Flask, jsonify, render_template
#import crud
from jinja2 import StrictUndefined
#import server
#os.system('dropdb tarot')
os.system('createdb tarot')
db = SQLAlchemy()
#db.create_all()
# seed_database

print("seeds!")

def create_cards():
    """Create cards from API"""
    #This is the request that gets all the cards from the API
    server_cards3 = requests.get('https://rws-cards-api.herokuapp.com/api/v1/cards/')
    #this turns the json into a dictionary
    api_cards = server_cards3.json()
    for x in range(78):
        api_cardsx = api_cards['cards'][x]
        card_name = api_cardsx['name']
        #card_name_short = api_cardsx['name_short']
        card_number = api_cardsx['value_int'] 
        card_desc = api_cardsx['desc']
        card_meaning_up = api_cardsx['meaning_up']
        card_meaning_reversed = api_cardsx['meaning_rev']
        card_type = api_cardsx['type'] 
        if card_type == 'minor':
            card_suit = api_cardsx['suit']
        else: 
            card_suit = None
        value = str(api_cards['cards'][x]['value_int'])
        
        """this figures out if the card's value integer is one digit or two,
            if the card type is major or minor, the suit, and then creates the correct
            naming convention to pull the correct image from the server
        """
        if len(value) == 1:
            value = "0" + value
        if card_type == "major":
                card_image = "static/cards/m" + value + ".jpg"
        elif card_type == "minor":
                suit_char = card_suit[0]
                card_image = "static/cards/" + suit_char + value + ".jpg" 
        
        print(card_name, card_number, card_desc, card_image)
        
        card = Card(card_name=card_name, 
                    card_number=card_number, 
                    card_meaning_up=card_meaning_up, 
                    card_meaning_reversed=card_meaning_reversed,
                    card_desc=card_desc, 
                    card_suit=card_suit,
                    card_type=card_type,
                    card_image=card_image
                    )
        db.session.add(card)
        db.session.commit()

def create_3_card_spread():
    spread_name = 3
    qty_cards_in_spread = 3

    spread = Spread(spread_id=3,
                    spread_name=spread_name,
                    qty_cards_in_spread=qty_cards_in_spread)
    
    db.session.add(spread)
    db.session.commit()

class Card(db.Model):
    """Class for each card in Database"""

    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False,
                        unique=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.deck_id'))                   
    card_name = db.Column(db.String(25),
                        nullable=False)
    card_number = db.Column(db.String(25))
    card_meaning_up = db.Column(db.Text)
    card_meaning_reversed = db.Column(db.Text)
    card_desc = db.Column(db.Text)
    card_suit = db.Column(db.String)
    card_type = db.Column(db.String)
    card_image = db.Column(db.String)

    card_readings_card = db.relationship("CardReading", backref="cards")
    
    def __repr__(self):
        """Show info about a card"""
        return f"<Card card_id={self.card_id} card_name={self.card_name}>"

class Deck(db.Model):
    """Data model for a Deck."""

    __tablename__ = 'decks'

    deck_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False,
                        unique=True)
    deck_name = db.Column(db.String(200),
                        nullable=False)
    deck_type = db.Column(db.String(200),
                        nullable=False)
    number_of_cards = db.Column(db.Integer)

    card_id = db.relationship('Card', backref='decks')

    def __repr__(self):
        """Show info about Decks."""
        return f"<Deck deck_id={self.deck_id} deck_name={self.deck_name}>"

class Spread(db.Model):
    """Data model for a Spread"""

    __tablename__ = 'spreads'

    spread_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False,
                        unique=True)
    spread_name = db.Column(db.String(200),
                        nullable=False)
    qty_cards_in_spread = db.Column(db.Integer,
                        nullable=False)

    reading = db.relationship("Reading", backref="spreads")
    
    def __repr__(self):
        """Show info about Spreads."""
       
        return f"<Spread spread_id={self.spread_id} spread_name={self.spread_name}>"

class User(db.Model):
    """Class of users"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        unique=True)
    user_name = db.Column(db.String(50))

    reading = db.relationship("Reading", backref="users")

    def __repr__(self):
        """Show info about Users."""
        return f"<user_id={self.user_id} user_name={self.user_name}>"

class Reading(db.Model):

    """Data model for all unique Readings."""

    __tablename__ = 'readings'

    reading_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        unique=True)
    reading_name = db.Column(db.String,
                            nullable=False)
    spread_id = db.Column(db.Integer, 
                        db.ForeignKey('spreads.spread_id'))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    
    #reading_card = db.Column(db.Integer, 
    #                     db.ForeignKey('cardreadings.card_reading_id'))

    #card_readings_cards = db.relationship("CardReading", backref="readings")

    def __repr__(self):
        """Show info about Reading."""
        return f"<reading_id={self.reading_id} reading_name={self.reading_name}>"

class CardReading(db.Model):
    """Table to store cards in spread"""

    __tablename__ = 'cardreadings'
    
    card_reading_id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True,
                    nullable=False,
                    unique=True)
    reading_id = db.Column(db.Integer,
                            db.ForeignKey('readings.reading_id'))
    card_id = db.Column(db.Integer,
                            db.ForeignKey('cards.card_id'))
    card_orient = db.Column(db.String,
                            nullable=False)

    card = db.relationship('Card', backref="cardreadings")
    
    #reading = db.relationship('Reading', backref="cardreadings")
    # Reading.query.filterby(reading_id=cardreading.reading_id) --> Reading associated

     
    def __repr__(self):

        return f"<CardReading card_reading_id={self.card_reading_id}>"


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///tarot'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
    db.app = app
    db.init_app(app)

    print('Connected to DB!')

if __name__ == '__main__':
    #from server import app
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "dev"
    app.jinja_env.undefined = StrictUndefined
    
    #connect_to_db(db.app)
    #db.create_all()
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    #print("HERE?")
    connect_to_db(app)
    #print("This one")
    
    db.create_all()
    create_3_card_spread()
    create_cards()
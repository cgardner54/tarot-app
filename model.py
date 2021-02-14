""" Data Model for Tarot-app """
import os
from flask_sqlalchemy import SQLAlchemy
os.system('dropdb tarot')
os.system('createdb tarot')
db = SQLAlchemy()

#import seed_database

print("seeds!")


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
    card_desc = db.Column(db.Text)
    card_reversed_desc = db.Column(db.Text)
    card_suit = db.Column(db.String)
    card_image = db.Column(db.String)

    #card_readings_card = db.relationship("CardReading", backref="cards")
    
    def __repr__(self):
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
    from server import app
    from flask import Flask

    #connect_to_db(db.app)
    #db.create_all()
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    #print("HERE?")
    #connect_to_db(app)
    #print("This one")
    
    #db.create_all()
    
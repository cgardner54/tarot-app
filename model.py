""" Data Model for Tarot-app """

from flask_sqlalchemy import SQLAlchemy
import seed_database

db = SQLAlchemy()

class Card(db.Model):
    """Class for each card in Database"""

    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.deck_id'))                   
    card_name = db.Column(db.String(25),
                        nullable=False)
    card_number = db.Column(db.String(25))
    card_desc = db.Column(db.Text)
    card_reversed_desc = db.Column(db.Text)
    card_suit = db.Column(db.String)
    card_image = db.Column(db.String)

    #card_deck = db.relationship('Deck', backref='decks')
    
    def __repr__(self):
        return f"<Card card_id={self.card_id} card_name={self.card_name}>"

class Deck(db.Model):
    """Data model for a Deck."""

    __tablename__ = 'decks'

    deck_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False)
    deck_name = db.Column(db.String(200),
                        nullable=False)
    deck_type = db.Column(db.String(200),
                        nullable=False)
    number_of_cards = db.Column(db.Integer)

    #deck_card_id = db.relationship('Card', backref='decks')

    def __repr__(self):
        """Show info about Decks."""
        return f"<Deck deck_id={self.deck_id} deck_name={self.deck_name}>"

class Spread(db.Model):
    """Data model for a Spread"""

    __tablename__ = 'spreads'

    spread_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False)
    spread_name = db.Column(db.String(200),
                        nullable=False)
    qty_cards_in_spread = db.Column(db.Integer,
                        nullable=False)
    
    def __repr__(self):
        """Show info about Spreads."""
       
        return f"<Spread spread_id={self.spread_id} spread_name={self.spread_name}>"

class User(db.Model):
    """Class of users"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    user_name = db.Column(db.String(50))

    def __repr__(self):
        """Show info about Users."""
        return f"<user_id={self.user_id} user_name={self.user_name}>"

# class Readings(db.Model):

#     """Data model for all unique Readings."""

#     __tablename__ = 'readings'

#     reading_id = db.Column(db.Integer, 
#                         primary_key=True, 
#                         autoincrement=True)
#     spread_id = db.Column(db.Integer, 
#                         db.ForeignKey('spreads.spread_id'))
#     card_reading_id = db.Column(db.Integer, 
#                         db.ForeignKey('card_reading.card_reading_id'))
#     user_id = db.Column(db.Integer,
#                         db.ForeignKey('users.user_id'))

    
    
#     readings_spreads = db.relationship("Spreads", foreign_keys="spreads.spread_id", backref="readings")
#     readings_users = db.relationship("User", foreign_keys="users.user_id", backref="readings")
#     card_readings = db.relationship("CardReading", foreign_keys="card_reading.card_reading_id", backref="readings")
#     def __repr__(self):
#         """Show info about Reading."""
#         return f"<reading_id={self.reading_id} card_reading_id={self.card_reading_id}>"

# class CardReading(db.Model):
#     """Table to store cards in spread"""

#     ___tablename__ = 'card_reading'
    
#     card_reading_id = db.Column(db.Integer, 
#                     primary_key=True, 
#                     autoincrement=True)
#     reading_id = db.Column(db.Integer,
#                             db.ForeignKey('readings.reading_id'))
#     card_id = db.Column(db.Integer,
#                             db.ForeignKey('cards.card_id'))

#     cards = db.relationship('Cards', foreign_keys="card_id", backref='card_reading')
#     reading = db.relationship('Readings', foreign_keys="reading_id",backref='card_reading')
#     def __repr__(self):

#         return f"<card_reading_id={self.card_reading_id}>"


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///tarot'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app
    from flask import Flask

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
    seed_database.create_seeds()
    print(seed_database.create_seeds())

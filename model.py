""" Data Model for Tarot-app """

from flask_sqlalchemy import SQLAlchemy
import seed_database

db = SQLAlchemy()


class Cards(db.Model):
    """Class for each card in Database"""

    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False)
    deck_id = db.Column(db.Integer, 
                        ForeignKey="decks.deck_id", 
                        autoincrement=True)
    card_name = db.Column(db.String(25),
                        nullable=False)
    card_number = db.Column(db.String(25)
                        #nullable=False
                        )
    card_desc = db.Column(db.Text
                        #nullable=False
                        )
    card_reversed_desc = db.Column(db.Text)
    card_suit = db.Column(db.String)
    card_image = db.Column(db.String)

    decks = db.relationship('Decks', backref='cards')

    def __repr__(self):
        """Show info about cards."""

        return f"<card_id={self.card_id} card_name={self.card_name}>"

class Decks(db.Model):
    """Data model for a Deck."""

    __tablename__ = 'decks'

    deck_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    deck_name = db.Column(db.String(200),
                        nullable=False)
    deck_type = db.Column(db.String(200),
                        nullable=False)
    number_of_cards = db.Column(db.Integer)

    def __repr__(self):
        """Show info about Decks."""
        return f"deck_id={self.deck_id} deck_name={self.deck_name}>"

class Spreads(db.Model):
    """Data model for a Spread"""

    __tablename__ = 'spreads'

    spread_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    spread_name = db.Column(db.String(200),
                        nullable=False)
    qty_cards_in_spread = db.Column(db.Integer)
    
    def __repr__(self):
        """Show info about Spreads."""
        return f"<spread_id={self.spread_id} spread_name={self.spread_name}>"
    
class CardGroup(db.Model):
    "Table to store cards in spread"

    ___tablename__ = 'card_groups'
    
    card_group_id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)
    spread_id = dbColumn(db.Integer,
                            db.ForeignKey('spreads.spread_id'))
    card_in_reading_0 = dbColumn(db.Integer,
                            db.ForeignKey('cards.card_id'))
    card_in_reading_1 = dbColumn(db.Integer,
                            db.ForeignKey('cards.card_id'))
    card_in_reading_2 = dbColumn(db.Integer,
                            db.ForeignKey('cards.card_id'))

    cards = db.relationship('Cards', backref='card_groups')

    def __repr__(self):
    
    """Show info about card_groups."""

    return f"<card_group_id={self.card_group_id} 
            card_in_reading_0={self.card_in_reading_0} 
            card_in_reading_2={self.card_in_reading_2}>"
     
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    user_name = db.Column(db.String(50))

    def __repr__(self):
        """Show info about Users."""
        return f"<user_id={self.user_id} user_name={self.user_name}>"

class Readings(db.Model):

    """Data model for all unique Readings."""

    __tablename__ = 'readings'

    reading_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    spread_id = db.Column(db.Integer, 
                        db.ForeignKey('spreads.spread_id'))
    card_group_id = db.Column(db.Integer, 
                        db.ForeignKey('card_group.card_group_id'))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    users = relationship("User", backref="readings")
    card_groups = relationship("CardGroup", backref="readings")
    spreads = relationship("Spreads", backref="readings")

    def __repr__(self):
        """Show info about Reading."""
        return f"<reading_id={self.spread_id} card_group_id={self.card_group_id}>"

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///tarot'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')

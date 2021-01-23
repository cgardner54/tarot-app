""" Data Model for Tarot-app """


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cards(db.Model):
    """Class for each card in Database"""
    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True,
                        nullable=False)
    card_name = db.Column(db.String(25),
                        nullable=False)
    card_type = db.Column(db.String(25)
                        #nullable=False
                        )
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
    card_id = db.Column(db.Integer, 
                        db.ForeignKey('cards.card_id'),
                        nullable=False)
    deck_name = db.Column(db.String(200),
                        nullable=False)
    number_of_cards = db.Column(db.Integer)

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

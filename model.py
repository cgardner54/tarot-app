""" Data Model for Tarot-app """


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cards(db.Model):
    """Class for each card in Database"""
    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    card_name = db.Column(db.String(25),
                        nullable=False)
    card_type = db.Column(db.String(25),
                        nullable=False)
    card_number = db.Column(db.String(25),
                        nullable=False)
    card_desc = db.Column(db.Text,
                        nullable=False)
    card_reversed_desc = db.Column(db.Text,
                        nullable=False)
    card_suit = db.Column(db.String)
    card_image = db.Column(db.String)

    animals = db.relationship('Animal', backref='humans')

    def __repr__(self):
        """Show info about humans."""

        return f"<human_id={self.human_id} fname={self.fname} lname={self.lname} email={self.email}>"

class Animal(db.Model):
    """Data model for an animal."""

    __tablename__ = 'animals'

    animal_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    human_id = db.Column(db.Integer, 
                        db.ForeignKey('humans.human_id'),
                        nullable=False)
    name = db.Column(db.String(50),
                        nullable=False)
    animal_species = db.Column(db.String(25),
                        nullable=False)
    birth_year = db.Column(db.Integer,
                        nullable=True)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
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

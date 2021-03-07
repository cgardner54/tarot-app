from sqlalchemy.sql.expression import func
from random import choices, sample, randint
from model import db, connect_to_db, Card, Spread, Deck, Reading, CardReading, User

def reading(spread_id):

    reading = Reading(randint=reading_id, spread_id=spread_id)

    db.session.add(reading)
    db.session.commit()

    return reading
def card_reading(reading_id, card_id):

    card_reading = CardReading(reading_id=reading_id, card_id=card_id)

    db.session.add(card_reading)
    db.session.commit()

    return card_reading


def create_user(user_name):

    user = User(user_name=user_name)

    db.session.add(user)
    db.session.commit()

    return user

def create_deck(deck_name, deck_type, number_of_cards):
    
    deck = Deck(deck_name=deck_name, deck_type=deck_type, number_of_cards=number_of_cards)

    db.session.add(deck)
    db.session.commit()

    return deck

def get_cards():
    cards = sample(Card.query.all(),3)
    print(cards)
    Card.query.all()
    return cards

#pusedo-code here
# def select_cards_3(deck_name=tarot):
#     reading = []
#     reading = random.sample(deck_id(1), 3)
#     return reading, reading_id, cardids


# def deck(deck_name):
#     """Return the human with the id 2."""
#     return (CardReading.query.card_id.all(reading_id=1))
#     """create a reading"""
#     """create a spread"""
#     """create a cardreading"""

#     """for a given reading, return cards in spread"""
#     """
#     # Functions start here!"""

#     """Return all cards in a three card reading"""
#     """Return all readings for a User"""
#     """Return a specific reading for a User"""
#     """Return all cards in a DECK"""
#     """Show all names for decks"""
#     """




if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
    print("CRUD connected!")
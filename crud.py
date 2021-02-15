from sqlalchemy.sql.expression import func
from random import choices, sample
from model import db, connect_to_db, Card, Spread, Deck, Reading, CardReading, User
def create_user(user_name):

    user = User(user_name=user_name)

    db.session.add(user)
    db.session.commit()

    return user

def create_card(card_name, deck_id, card_number, card_desc, card_reversed_desc, card_suit, card_image):
    """Create and return a new user."""

    card = Card(card_name=card_name, deck_id=deck_id, card_number=card_number, card_desc=card_desc,card_reversed_desc=card_reversed_desc, card_suit=card_suit, card_image=card_image)

    db.session.add(card)
    db.session.commit()

    return card

def create_deck(deck_name, deck_type, number_of_cards):
    
    deck = Deck(deck_name=deck_name, deck_type=deck_type, number_of_cards=number_of_cards)

    db.session.add(deck)
    db.session.commit()

    return deck

def get_cards():
    cards = Card.query.all()
    return sample(Card.query.all(),3)

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

# # def get_first_fish():
# #     """Return the FIRST animal with the species 'fish'."""
# #     return Animal.query.filter_by(animal_species='fish').first()

# # def get_young_animals():
# #     """Return all animals that were born after 2015.

# #     Do NOT include animals without birth years.
# #     """
# #     young_animals = Animal.query.filter(birth_year > 2015).all()
# #     return young_animals

# #         ### I can't figure out why my operators are not working.
    

# # def get_j_names():
# #     """Return the humans with first names that start with 'J'."""
# #     return Human.query.filter(fname='J%').all

# #     #not sure how to index into the fname... for J.

# # def get_null_bdays():
# #     """Return all animals whose birth years are NULL."""

# #     return Animal.query.filter(birth_year = None).all()

# # def get_fish_or_rabbits():
# #     """Return all animals whose species is 'fish' OR 'rabbit'."""
# #     fish = Animal.query.filter_by(animal_species='fish').all()
# #     rabbit = Animal.query.filter_by(animal_species='rabbit').all()
# #     return fish, rabbit
# #     #I can't figure out why my operators are not working. Would've liked to do this in one line

# # def print_directory():
# #     """Output a list of humans and their animals.

# #     For example:

# #     >>> print_directory()
# #     Justin Time
# #     - Peter (rabbit)
# #     - Peppa (pig)
# #     Carmen Sandiego
# #     - Blub (fish)

# #     You may only use ONE query to retrieve initial data. (Hint: leverage a
# #     SQLAlchemy relationship to retrieve additional information)
# #     """


# # def find_humans_by_animal_species(species):
# #     """Return a list of all humans who have animals of the given species.

# #     Each human should only appear once in the returned list. For example:

# #     >>> find_humans_by_animal_species('snake')

# #     Again, you may only use ONE query to retrieve initial data. (Hint: use a
# #     relationship! Also, you can pursue uniqueness in a Pythonic way --- you
# #     don't have to do it with pure SQLAlchemy)
# #     """


if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
    print("query connected!")
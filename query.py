"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.
"""

from model import db, Cards, Spreads, Decks


def get_human_2():
    """Return the human with the id 2."""
    return (Human.query.get(2))


def get_first_fish():
    """Return the FIRST animal with the species 'fish'."""
    return Animal.query.filter_by(animal_species='fish').first()

def get_young_animals():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """
    young_animals = Animal.query.filter(birth_year > 2015).all()
    return young_animals

        ### I can't figure out why my operators are not working.
    

def get_j_names():
    """Return the humans with first names that start with 'J'."""
    return Human.query.filter(fname='J%').all

    #not sure how to index into the fname... for J.

def get_null_bdays():
    """Return all animals whose birth years are NULL."""

    return Animal.query.filter(birth_year = None).all()

def get_fish_or_rabbits():
    """Return all animals whose species is 'fish' OR 'rabbit'."""
    fish = Animal.query.filter_by(animal_species='fish').all()
    rabbit = Animal.query.filter_by(animal_species='rabbit').all()
    return fish, rabbit
    #I can't figure out why my operators are not working. Would've liked to do this in one line

def print_directory():
    """Output a list of humans and their animals.

    For example:

    >>> print_directory()
    Justin Time
    - Peter (rabbit)
    - Peppa (pig)
    Carmen Sandiego
    - Blub (fish)

    You may only use ONE query to retrieve initial data. (Hint: leverage a
    SQLAlchemy relationship to retrieve additional information)
    """


def find_humans_by_animal_species(species):
    """Return a list of all humans who have animals of the given species.

    Each human should only appear once in the returned list. For example:

    >>> find_humans_by_animal_species('snake')

    Again, you may only use ONE query to retrieve initial data. (Hint: use a
    relationship! Also, you can pursue uniqueness in a Pythonic way --- you
    don't have to do it with pure SQLAlchemy)
    """


if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)

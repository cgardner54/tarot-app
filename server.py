"""Server file for tarot app
"""
import requests, random
from Imageflip import flip_mirror
from PIL import Image, ImageOps 
from flask import Flask, jsonify, render_template
from model import connect_to_db, Card, Deck, Spread, User, Reading, CardReading
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

"""
Create a class called cards
here we would have a method to call a card, number it and determine if it should
be upside down or not
we should also pull in the title, and meaning
iif the card is upside down, add the class tag to it, with a value reversed or not.
"""
#class Card:


def find_image_name(api_cards,card_position):
        card_type = api_cards['cards'][card_position]['type']
        value = str(api_cards['cards'][card_position]['value_int'])
        """this figures out if the card's value integer is one digit or two,
            if the card type is major or minor, the suit, and then creates the correct
            naming convention to pull the correct image from the server
        """
        if len(value) == 1:
            value = "0" + value
        if card_type == "major":
                img_name = "static/cards/m" + value + ".jpg"
                return img_name
        elif card_type == "minor":
                suit = str(api_cards['cards'][card_position]['suit'])
                suit_char = suit[0]
                img_name = "static/cards/" + suit_char + value + ".jpg"
                return img_name

def orient_the_card():
    """This randomly decides what direction the card should appear.
        Cards have a 1/4 chance of being reversed."""
    random_number = random.randint(0, 3)
    if random_number == 0:
        return "meaning_rev"
    else:
        return "meaning_up"


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')

@app.route('/three_card_spread')
def three_card_page():
    """show a three card spread"""
    
@app.route('/api/cards/<int:card_id>')
def card(card_id):
    """Return a human from the database as JSON."""

    card = Card.query.get(card_id)

    if card:
        cards = {'status': 'success',
                'card_id': card.card_id,
                'card_name': card.card_name}
        return jsonify(cards)
    else:
        return jsonify({'status': 'error',
                        'message': 'No card found with that ID'})

@app.route('/api/decks/<int:deck_id>')
def deck(deck_id):
    """Return a human from the database as JSON."""

    deck = Deck.query.get(deck_id)

    if deck:
        return jsonify({'status': 'success',
                        'deck_id': deck.deck_id,
                        'deck_name': deck.deck_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No deck found with that ID'})

@app.route('/api/spreads/<int:spread_id>')
def spread(spread_id):
    """Return a spread from the database as JSON."""

    spread = Spread.query.get(spread_id)

    if spread:
        return jsonify({'status': 'success',
                        'spread_id': spread.spread_id,
                        'spread_name': spread.spread_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No spread found with that ID'})

@app.route('/api/users/<int:user_id>')
def user(user_id):
    """Return a spread from the database as JSON."""

    user = User.query.get(user_id)

    if user:
        return jsonify({'status': 'success',
                        'user_id': user.spread_id,
                        'user_name': user.spread_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No spread found with that ID'})

@app.route('/api/readings/<int:reading_id>')
def reading(reading_id):
    """Return a reading from the database as JSON."""

    reading = Reading.query.get(reading_id)

    if reading:
        return jsonify({'status': 'success',
                        'reading_id': reading.reading_id,
                        'reading_name': reading.reading_name,
                        'reading_card:': reading.reading_card})
    else:
        return jsonify({'status': 'error',
                        'message': 'No reading found with that ID'})

@app.route('/api/cardreadings/<int:card_reading_id>')
def card_reading(card_reading_id):
    """Return a reading from the database as JSON."""

    card_reading = CardReading.query.get(card_reading_id)

    if card_reading:
        return jsonify({'status': 'success',
                        'card_reading_id': cardreading.card_reading_id,
                        'reading_id': cardreading.reading_id})
    else:
        return jsonify({'status': 'error',
                        'message': 'No reading found with that ID'})

@app.route('/cards')
def get_cards(position1=0, position2=1, position3=2):
    #this is the API request for three random cards
    server_cards3 = requests.get('https://rws-cards-api.herokuapp.com/api/v1/cards/random?n=3')
    #this turns the json into a dictionary
    api_cards = server_cards3.json()
    print(api_cards)
    """View three card."""
    img_name1 = find_image_name(api_cards, position1)
    img_name2 = find_image_name(api_cards, position2)

    img_name3 = find_image_name(api_cards, position3)


    orient_the_card1 = orient_the_card()
    orient_the_card2 = orient_the_card()
    orient_the_card3 = orient_the_card()
    card1 = api_cards['cards'][position1]['name']
    card1desc = api_cards['cards'][position1][orient_the_card1]
    card2 = api_cards['cards'][position2]['name']
    card2desc = api_cards['cards'][position2][orient_the_card2]
    card3 = api_cards['cards'][position3]['name']
    card3desc = api_cards['cards'][position3][orient_the_card3]

    #reading id here or card reading id to save the reading

    return render_template('cards.html', 
                            card1=card1, 
                            card2=card2, 
                            card3=card3, 
                            card1desc=card1desc,
                            card2desc=card2desc,
                            card3desc=card3desc,
                            img_name1=img_name1,
                            img_name2=img_name2,
                            img_name3=img_name3,
                            orient_the_card1=orient_the_card1,
                            orient_the_card2=orient_the_card2,
                            orient_the_card3=orient_the_card3
                            )

# @app.route('/threecards')
    
        
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

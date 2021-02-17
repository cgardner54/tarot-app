"""Server file for tarot app
"""
import requests
from flask import Flask, jsonify, render_template
from model import connect_to_db, Card, Deck, Spread, User, Reading, CardReading
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#this is the API request for three random cards
server_cards3 = requests.get('https://rws-cards-api.herokuapp.com/api/v1/cards/random?n=3')
#this turns the json into a dictionary
api_cards = server_cards3.json()
print(api_cards)

def find_image_name1(api_cards):
        card_type = api_cards['cards'][0]['type']
        value = str(api_cards['cards'][0]['value_int'])
        if len(value) == 1:
            value = "0" + value
        if card_type == "major":
                img_name = "static/cards/m" + value + ".jpg"
                return img_name
        elif card_type == "minor":
                suit = str(api_cards['cards'][0]['suit'])
                suit_char = suit[0]
                img_name = "static/cards/" + suit_char + value + ".jpg"
                return img_name

def find_image_name2(api_cards):
        card_type = api_cards['cards'][1]['type']
        value = str(api_cards['cards'][1]['value_int'])
        if len(value) == 1:
            value = "0" + value
        if card_type == "major":
                img_name = "static/cards/m" + value + ".jpg"
                return img_name
        elif card_type == "minor":
                suit = str(api_cards['cards'][1]['suit'])
                suit_char = suit[0]
                img_name = "static/cards/" + suit_char + value + ".jpg"
                return img_name

def find_image_name3(api_cards):
        card_type = api_cards['cards'][2]['type']
        value = str(api_cards['cards'][2]['value_int'])
        if len(value) == 1:
            value = "0" + value
        if card_type == "major":
                img_name = "static/cards/m" + value + ".jpg"
                return img_name
        elif card_type == "minor":
                suit = str(api_cards['cards'][2]['suit'])
                suit_char = suit[0]
                img_name = "static/cards/" + suit_char + value + ".jpg"
                return img_name
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
def get_cards():
    """View three card."""
    img_name1 = find_image_name1(api_cards)
    img_name2 = find_image_name2(api_cards)
    img_name3 = find_image_name3(api_cards)
    print(img_name1)
    print(img_name2)
    print(img_name3)
    card1 = api_cards['cards'][0]['name']
    card1desc = api_cards['cards'][0]['meaning_up']
    card2 = api_cards['cards'][1]['name']
    card2desc = api_cards['cards'][1]['meaning_up']
    card3 = api_cards['cards'][2]['name']
    card3desc = api_cards['cards'][2]['meaning_up']
        
    return render_template('cards.html', 
                            card1=card1, 
                            card2=card2, 
                            card3=card3, 
                            card1desc=card1desc,
                            card2desc=card2desc,
                            card3desc=card3desc,
                            img_name1=img_name1,
                            img_name2=img_name2,
                            img_name3=img_name3
                            )

# @app.route('/threecards')
    
        
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

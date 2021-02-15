"""Server file for tarot app
"""

from flask import Flask, jsonify, render_template
from model import connect_to_db, Card, Deck, Spread, User, Reading, CardReading
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

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
    """View one card."""

    server_cards = crud.get_cards()
    print(server_cards)
    three_card_dict = {"card1name":  server_cards[0].card_name,
                        "card2name":  server_cards[1].card_name,
                        "card3name":  server_cards[2].card_name
                        }
    card1 = three_card_dict.get("card1name")
    card2 = three_card_dict.get("card2name")
    card3 = three_card_dict.get("card3name")
    #json_three_card_dict = jsonify(three_card_dict)
    return render_template('cards.html', card1=card1, card2=card2, card3=card3)

        

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

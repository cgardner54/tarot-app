"""Server file for tarot app
"""

from flask import Flask, jsonify, render_template
from model import connect_to_db, Card, Deck, Spread, User#, Readings, CardReading


app = Flask(__name__)


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')


@app.route('/api/cards/<int:card_id>')
def card(card_id):
    """Return a human from the database as JSON."""

    card = Card.query.get(card_id)

    if card:
        return jsonify({'status': 'success',
                        'card_id': cards.card_id,
                        'card_name': cards.card_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No hcarduman found with that ID'})

@app.route('/api/decks/<int:deck_id>')
def deck(deck_id):
    """Return a human from the database as JSON."""

    deck = Deck.query.get(deck_id)

    if deck:
        return jsonify({'status': 'success',
                        'deck_id': decks.deck_id,
                        'deck_name': decks.deck_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No deck found with that ID'})

@app.route('/api/spreads/<int:spread_id>')
def spread(spread_id):
    """Return a spread from the database as JSON."""

    spread = Spread.query.get(spread_id)

    if spread:
        return jsonify({'status': 'success',
                        'spread_id': spreads.spread_id,
                        'spread_name': spreads.spread_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No spread found with that ID'})

@app.route('/api/users/<int:user_id>')
def user(user_id):
    """Return a spread from the database as JSON."""

    user = User.query.get(user_id)

    if user:
        return jsonify({'status': 'success',
                        'user_id': spreads.spread_id,
                        'user_name': spreads.spread_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No spread found with that ID'})

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

"""Server file for tarot app
"""

from flask import Flask, jsonify, render_template
from model import connect_to_db, Cards#, Decks, Spreads, User, Readings, CardReading


app = Flask(__name__)


@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')


@app.route('/api/cards/<int:card_id>')
def card(card_id):
    """Return a human from the database as JSON."""

    card = Cards.query.get(card_id)

    if card:
        return jsonify({'status': 'success',
                        'card_id': cards.card_id,
                        'card_name': cards.card_name})
    else:
        return jsonify({'status': 'error',
                        'message': 'No hcarduman found with that ID'})


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

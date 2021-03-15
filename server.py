"""Server file for tarot app
"""
import requests, random
from Imageflip import flip_mirror
from PIL import Image, ImageOps 
from flask import Flask, jsonify, render_template, redirect, url_for
from model import db, connect_to_db, Card, Deck, Spread, User, Reading, CardReading
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

def orient_the_card():
    """This randomly decides what direction the card should appear.
        Cards have a 1/4 chance of being reversed."""
    random_number = random.randint(0, 1)
    if random_number == 0:
        return "card_meaning_reversed"
    else:
        return "card_meaning_up"

@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template('index.html')

@app.route('/login')
def login():
    """Show the login page."""

    return render_template('login.html')
    
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

 
@app.route('/api/cardreading/<card1>')
def card_reading(reading_id):
    # Psuedocode
    #    card1 = Reading.query.get(cardreading.card)
    #    card2 = 
    """Return a reading from the database as JSON."""

    card_reading = CardReading.query.get(card_reading_id)

    if card_reading:
        return jsonify({'status': 'success',
                        'card_reading_id': cardreading.card_reading_id,
                        'reading_id': cardreading.reading_id})
    else:
        return jsonify({'status': 'error',
                        'message': 'No reading found with that ID'})

@app.route('/threecards/<int:reading_id>')
def three_card_reading(reading_id):
    """This will redirect to the user's card_reading"""
    reading_id_from_crud = crud.Reading.query.get(reading_id)
    print(reading_id_from_crud)
    card_reading_from_crud = CardReading.query.filter(CardReading.reading_id == reading_id).all()
    
    print("****"*15)
    print(card_reading_from_crud)

    print("^^^^^^"*15)
    """ Card Ids from reading"""
    cardreading_card1_card_id = card_reading_from_crud[0].card_id
    cardreading_card2_card_id = card_reading_from_crud[1].card_id
    cardreading_card3_card_id = card_reading_from_crud[2].card_id

    """ card images """
    card1_image = crud.get_card_by_id(cardreading_card1_card_id).card_image
    card2_image = crud.get_card_by_id(cardreading_card2_card_id).card_image
    card3_image = crud.get_card_by_id(cardreading_card3_card_id).card_image

    """ Card Name"""
    card1_name = crud.get_card_by_id(cardreading_card1_card_id).card_name
    card2_name = crud.get_card_by_id(cardreading_card2_card_id).card_name
    card3_name = crud.get_card_by_id(cardreading_card3_card_id).card_name
    
    """card orientation"""
    cardreading_card1_orient = card_reading_from_crud[0].card_orient
    cardreading_card2_orient = card_reading_from_crud[1].card_orient
    cardreading_card3_orient = card_reading_from_crud[2].card_orient

    """card meaning"""
    card1_meaning = crud.get_card_by_id(cardreading_card1_card_id).card_meaning_up
    if cardreading_card1_orient == "card_meaning_reversed":
        card1_meaning = crud.get_card_by_id(cardreading_card1_card_id).card_meaning_reversed

    card2_meaning = crud.get_card_by_id(cardreading_card2_card_id).card_meaning_up
    if cardreading_card2_orient == "card_meaning_reversed":
        card2_meaning = crud.get_card_by_id(cardreading_card2_card_id).card_meaning_reversed
    
    card3_meaning = crud.get_card_by_id(cardreading_card3_card_id).card_meaning_up
    if cardreading_card3_orient == "card_meaning_reversed":
        card3_meaning = crud.get_card_by_id(cardreading_card3_card_id).card_meaning_reversed


    """hide the footer!"""
    reveal = "footer_hide"
    return render_template("cards.html",
                            reading_id=reading_id_from_crud,
                            card1_name=card1_name,
                            card1_image=card1_image,
                            card1_meaning=card1_meaning,
                            orient1=cardreading_card1_orient,
                            card2_name=card2_name,
                            card2_image=card2_image,
                            card2_meaning=card2_meaning,
                            orient2=cardreading_card2_orient,
                            card3_name=card3_name,
                            card3_image=card3_image,
                            card3_meaning=card3_meaning,
                            orient3=cardreading_card3_orient,
                            reveal=reveal
                            )

@app.route('/get_cards_function/')
def get_cards():
    """View three card."""

    crud_3 = crud.get_cards()
    """create spreads and readings"""
    spread_name = 3
    spread_id = crud.get_three_card_spread()
    reading_id = crud.create_reading(spread_name, spread_id).reading_id
    
    """Select the orientation of the cards, reversed or upright"""
    card_orient0 = orient_the_card()
    card_orient1 = orient_the_card()
    card_orient2 = orient_the_card()

    """submit the reading information to card_reading table, 
        Allows user to recreate the reading if they'd like to"""
    card_reading1 = crud.card_reading(reading_id, crud_3[0].card_id, card_orient0)
    card_reading2 = crud.card_reading(reading_id, crud_3[1].card_id, card_orient1)
    card_reading3 = crud.card_reading(reading_id, crud_3[2].card_id, card_orient2)
    
    """Create the variables to pass to HTML for each card, 
                Cards will now be refered to their position number, 1,2,3 instead of index 0,1,2
    """
    #Card1
    card1_image = crud_3[0].card_image
    card1_name = crud_3[0].card_name
    card1_meaning = crud_3[0].card_meaning_up
    orient1 = card_orient0
    if orient1 == "card_meaning_reversed":
        card1_meaning = crud_3[0].card_meaning_reversed
    #Card2
    card2_image = crud_3[1].card_image
    card2_name = crud_3[1].card_name
    card2_meaning = crud_3[1].card_meaning_up
    orient2 = card_orient1
    if orient2 == "card_meaning_reversed":
        card2_meaning = crud_3[1].card_meaning_reversed
    
    #Card3
    card3_image = crud_3[2].card_image
    card3_name = crud_3[2].card_name
    card3_meaning = crud_3[2].card_meaning_up
    orient3 = card_orient2
    if orient3 == "card_meaning_reversed":
        card3_meaning = crud_3[2].card_meaning_reversed
    
    """render template and pass variables to the HTML macros"""
    return render_template('cards.html', reading_id=reading_id,
                            card1_name=card1_name,
                            card1_image=card1_image,
                            card1_meaning=card1_meaning,
                            orient1=orient1,
                            card2_name=card2_name,
                            card2_image=card2_image,
                            card2_meaning=card2_meaning,
                            orient2=orient2,
                            card3_name=card3_name,
                            card3_image=card3_image,
                            card3_meaning=card3_meaning,
                            orient3=orient3,
                            reveal="footer"
                            )
        
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

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

def orient_the_card(position=0):
    """This randomly decides what direction the card should appear.
        Cards have a 1/4 chance of being reversed."""
    meaning_rev = crud_3[0].card_meaning_reversed
    meaning_up = crud_3[0].card_meaning_up
    random_number = random.randint(0, 3)
    if random_number == 0:
        return meaning_rev
    else:
        return meaning_up

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
    card_reading_from_crud = crud.CardReading.query.filter(reading_id)
    
    print("****"*15)
    print(card_reading_from_crud)

    print("^^^^^^"*15)
    cardreading_card1_id = card_reading_from_crud[0].card_id
    cardreading_card2_id = card_reading_from_crud[1].card_id
    cardreading_card3_id = card_reading_from_crud[2].card_id
    card1_image = crud.get_card_image(cardreading_card1_id)
    card2_image = crud.get_card_image(cardreading_card2_id)
    card3_image = crud.get_card_image(cardreading_card3_id)
    print("$$$"*25)
    print(card1_image)
    print(cardreading_card1_id)
    return render_template("saved_3card_spread.html", 
                            #card1=card1_card, 
                            card1_image=card1_image,
                            card2_image=card2_image,
                            card3_image=card3_image
                            #card1_meaning=card1_meaning,
                            )

@app.route('/get_cards_function/')
def get_cards(position1=0, position2=1, position3=2):
    
    """psuedocode for making readings.....
    """
    
    # orient_the_card1 = orient_the_card()
    # orient_the_card2 = orient_the_card()
    # orient_the_card3 = orient_the_card()
    """View three card."""
    crud_3 = crud.get_cards()
    """create spreads and readings"""
    spread_name = 3
    spread_id = crud.get_three_card_spread()
    reading_id = crud.create_reading(spread_name, spread_id).reading_id
    card_reading1 = crud.card_reading(reading_id, crud_3[0].card_id, crud_3[0].card_meaning_reversed) #, #orient_the_card1
    card_reading2 = crud.card_reading(reading_id, crud_3[1].card_id, crud_3[1].card_meaning_reversed)#, #orient_the_card2
    card_reading3 = crud.card_reading(reading_id, crud_3[2].card_id, crud_3[2].card_meaning_reversed)#, #orient_the_card3
    print("********")
    print(reading_id)

    #Card1
    card1_image = crud_3[0].card_image
    print (card1_image, "$$$$$$$")
    card1_name = crud_3[0].card_name
    card1_meaning = crud_3[0].card_meaning_up
    card1_meaning_rev = crud_3[0].card_meaning_reversed
    print("#######")
    
    #Card2
    card2_image = crud_3[1].card_image
    card2_name = crud_3[1].card_name
    card2_meaning = crud_3[1].card_meaning_up
    card2_meaning_rev = crud_3[1].card_meaning_reversed
    
    #Card3
    card3_image = crud_3[2].card_image
    card3_name = crud_3[2].card_name
    card3_meaning = crud_3[2].card_meaning_up
    card3_meaning_rev = crud_3[2].card_meaning_reversed
    
    return render_template('cards.html',reading_id=reading_id,
                            card1_name=card1_name,
                            card1_image=card1_image,
                            card1_meaning=card1_meaning,
                            card2_name=card2_name,
                            card2_image=card2_image,
                            card2_meaning=card2_meaning,
                            card3_name=card3_name,
                            card3_image=card3_image,
                            card3_meaning=card3_meaning,
                            card1_meaning_rev=card1_meaning_rev,
                            card2_meaning_rev=card2_meaning_rev,
                            card3_meaning_rev=card3_meaning_rev
                            )
        
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

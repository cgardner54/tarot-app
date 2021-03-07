"""Server file for tarot app
"""
import requests, random
from Imageflip import flip_mirror
from PIL import Image, ImageOps 
from flask import Flask, jsonify, render_template, redirect, url_for
from model import db, connect_to_db, Card, Deck, Spread, User, Reading, CardReading, create_3_card_spread
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

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



@app.route('/threecards/<string:card1>/<string:card2>/<string:card3>/<int:reading_id>')
def three_card_reading(card1, card2, card3):
    """This will redirect to the user's card_reading"""
    # reading_id = 12
    # crud_3 = crud.get_cards()
    # card1 = crud_3[0].card_name
    # card1_image = crud_3[0].card_image
    # card2 = crud_3[1].card_name
    # card3 = crud_3[3].card_name

    return render_template('cards.html', 
                            card1=card1, 
                            card2=card2, 
                            card3=card3, 
                            # card1desc=card1desc,
                            # card2desc=card2desc,
                            # card3desc=card3desc,
                            #img_name1=img_name1,
                            # img_name2=img_name2,
                            # img_name3=img_name3,
                            # orient_the_card1=orient_the_card1,
                            # orient_the_card2=orient_the_card2,
                            # orient_the_card3=orient_the_card3,
                            reading_id=reading_id
                            )

@app.route('/get_cards_function/')
def get_cards(position1=0, position2=1, position3=2):
    #app.route('/username=<username>&password=<password>')
    """psuedocode for making readings.....
    """
    # in crud.py : create_reading and card_reading 
    # use create_reading card_reading..... in server to send card info to /cards.html
    # html:
    #  button where the user can "save" a reading
    # action to bring you to the user_profile.html --> update the reading object to have a user_id !Null
        # save the reading to the user profile, and take you to user profile with list of past readings. 
    # have unique urls for each reading. 
    
    crud_3 = crud.get_cards()
    card1_name = crud_3[0].card_name
    card1_image = crud_3[0].card_image
    card2_name = crud_3[1].card_name
    card1_suit = crud_3[0].card_suit
    card3_name = crud_3[2].card_name
    card1_meaning =  crud_3[0].card_meaning_up
    print(crud_3)
    
    """View three card."""

    orient_the_card1 = orient_the_card()
    orient_the_card2 = orient_the_card()
    orient_the_card3 = orient_the_card()
   
    card1 = card1_name, card1_image, orient_the_card1
    card2 = card2_name, card2_image, orient_the_card2
    card3 = card3_name, card3_image, orient_the_card3
    reading_id = crud.create_reading(3)
    return redirect(url_for('three_card_reading', card1=card1_name,
                            card2=card2_name,
                            #img_name1=card1_image,
                            # # card2=card2, 
                            card3=card3_name, 
                            # #card1desc=card1desc,
                            # #card2desc=card2desc,
                            # #card3desc=card3desc,
                            # orient_the_card1=orient_the_card1,
                            # orient_the_card2=orient_the_card2,
                            # orient_the_card3=orient_the_card3,
                            reading_id=reading_id
                            ))
        
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, jsonify, request 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, values
from dbModel import Games

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser://@192.168.189.141/FLASK'
db = SQLAlchemy(app)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")

# The GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        print(post_data.get('played'))
        NewGame = Games(
                        title=post_data.get('title'), genre=post_data.get('genre'), played=post_data.get('played'))
        db.session.add(NewGame)
        db.session.commit()
        response_object['message'] =  'Game Added!'
    else:
        response_object['games'] = [i.serialize for i in Games.query.all()]
    return jsonify(response_object)


#The PUT and DELETE route handler
@app.route('/games/<game_id>', methods =['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        
        RemoveGame = delete(Games).where(Games.id == game_id)
        db.session.execute(RemoveGame)
        db.session.commit()

        NewGame = Games(
                        id=game_id, title=post_data.get('title'), genre=post_data.get('genre'), played=post_data.get('played'))
        db.session.add(NewGame)
        db.session.commit()
        
        response_object['message'] =  'Game Updated!'
        print(post_data.get('played'))
    if request.method == "DELETE":
        RemoveGame = delete(Games).where(Games.id == game_id)
        db.session.execute(RemoveGame)
        db.session.commit()
        response_object['message'] = 'Game removed!'    
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)


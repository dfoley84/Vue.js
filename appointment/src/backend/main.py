from flask import Flask, jsonify, request 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, values
from dbModel import Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser://@192.168.189.141/FLASK'
db = SQLAlchemy(app)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET', 'POST'])
def all_pets():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        print(post_data.get('played'))
    else:
        response_object['appointments'] = [i.serialize for i in Pet.query.all()]
    return jsonify(response_object)

#The PUT and DELETE route handler
@app.route('/<petName>', methods =['PUT','DELETE'])
def single_game(petName):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        RemovePet = delete(Pet).where(Pet.petName == petName)
        db.session.execute(RemovePet)
        db.session.commit()
        NewPet = Pet(
             id=post_data.get('id'), petName=post_data.get('petName'), petOwner=post_data.get('petOwner'), aptDate=post_data.get('aptDate'), aptNote=post_data.get('aptNote'))
        db.session.add(NewPet)
        db.session.commit()
    if request.method == "DELETE":
        print(petName)
        RemovePet = delete(Pet).where(Pet.petName == petName)
        db.session.execute(RemovePet)
        db.session.commit()
        response_object['message'] = 'Pet Removed!'    
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)


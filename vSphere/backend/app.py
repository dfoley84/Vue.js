from flask import Flask, jsonify, request 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, values
from dbModel import vCenter, Horizon

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser://@/vSphere'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

SQLALCHEMY_ENGINE_OPTIONS = {
    "max_overflow": 100,
    "pool_pre_ping": True,
    "pool_recycle": 160 * 160,
    "pool_size": 1000,
}

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#Get vDesks
@app.route('/horizon', methods=['GET'])
def GetvDesks():
    response_object = {'status': 'success'}
    response_object['vdesks'] = [i.serialize for i in Horizon.query.all()]
    db.session.remove()
    return jsonify(response_object)

  
#Get Searched vDesks based on User
@app.route("/searchdata", methods=['GET', 'POST'])
def searchdata():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Username = post_data.get('username')
        response_object['vdesks'] = [i.serialize for i in Horizon.query.filter_by(UserName=Username).all()]
        print(response_object['vdesks'])
        db.session.remove()
    return jsonify(response_object)

#Get vCenter Servers

#Get Searched vCenter Servers based on User

#Get VMWare on AWS


if __name__ == '__main__':
    app.run()

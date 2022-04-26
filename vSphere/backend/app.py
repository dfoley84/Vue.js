from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, values
from dbModel import vCenter, Horizon
from rabbitmq import RabbitMQ_Sender


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:'
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


#SQL Alchemy Functions
def DeleteMachine(MachineName):
    RemovevDesks = delete(Horizon).where(Horizon.MachineName == MachineName)
    db.session.execute(RemovevDesks)
    db.session.commit()
    db.session.remove()

def UpdateMachine(MachineName):
    db.session.query(Horizon).filter(Horizon.MachineName == MachineName).update({"MachineStatus": "Running Job"})
    db.session.commit()
    db.session.remove()



#Getting All vDesks
@app.route('/horizon', methods=['GET'])
def GetvDesks():
    response_object = {'status': 'success'}
    response_object['vdesks'] = [i.serialize for i in Horizon.query.all()]
    db.session.remove()
    return jsonify(response_object)



#Display vDesks from Searched User
@app.route("/searchdata", methods=['GET', 'POST'])
def searchdata():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Username = post_data.get('TitleUser')
        response_object['SearchvDesks'] = [i.serialize for i in Horizon.query.filter_by(UserName=Username).all()]
        db.session.remove()
    return jsonify(response_object)


#Display vDesks from Searched User
@app.route("/powercycle", methods=['GET','POST'])
def selectedMachine():
    response_object = {'status':'success'}
    if request.method == 'POST':
        message = request.get_json() #Getting Posted JSON Data

        #Getting Machine Information from FontEnd.
        PowerCycle = message['data']['PowerCycle']
        MachineName = message['data']['vDesk']['MachineName']

        RabbitMQ_Sender(message) #Passing Message to Class RabbitMQ_Sender
        requests.get("http://mircoservice_rabbitmq:5001/message") #Calling RabbitMQ_Receiver
        
        #Updating DB Based on PowerCycle
        if PowerCycle == 'Delete':
           DeleteMachine(MachineName)
        else:
            UpdateMachine(MachineName)
    return jsonify()


@app.route("/searchdata/powercycle", methods=['GET','POST'])
def PowerCycle():
    response_object = {'status':'success'}
    if request.method == 'POST':
        message = request.get_json() #Getting Posted JSON Data
        #Getting Machine Information from FontEnd.
        PowerCycle = message['PowerCycle']
        MachineName = message['vDesk']['MachineName']
        RabbitMQ_Sender(message) #Passing Message to Class RabbitMQ_Sender
        #Updating DB Based on PowerCycle
        if PowerCycle == 'Delete':
           DeleteMachine(MachineName)
        else:
            UpdateMachine(MachineName)
    return jsonify()


if __name__ == '__main__':
    app.run()

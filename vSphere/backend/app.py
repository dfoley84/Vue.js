from flask import Flask, jsonify, request 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, values
from dbModel import vCenter, Horizon
import pika, json 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser://@FLASK'
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


@app.route('/horizon', methods=['GET','POST'])
def GetvDesks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        #Getting Posted JSON Data 
        message = request.get_json()

        #Getting Machine Information from FontEnd.
        PowerCycle = message['PowerCycle']
        MachineName = message['vDesk']['MachineName']

        #Pass Information to RabbitMQ For Jenkins Jobs
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='vDeskPowerCycle', durable=False)
        channel.basic_publish(
            exchange='',
            routing_key='vDeskPowerCycle',
            body=json.dumps(message),
            properties=pika.BasicProperties(
            delivery_mode=2,
        ))
        connection.close()

        #Updating DB Based on PowerCycle
        if PowerCycle == 'Delete':
            RemovevDesks = delete(Horizon).where(Horizon.MachineName == MachineName)
            db.session.execute(RemovevDesks)
            db.session.commit()
        else:
            #Append Running Job to Machine Status.
            print('')
        
    else:
        response_object['vdesks'] = [i.serialize for i in Horizon.query.all()]
        db.session.remove()
    return jsonify(response_object)

#Get Searched User
@app.route("/searchdata", methods=['GET', 'POST'])
def searchdata():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Username = post_data.get('TitleUser')
        print(Username)
        response_object['SearchvDesks'] = [i.serialize for i in Horizon.query.filter_by(UserName=Username).all()]
        db.session.remove()
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()

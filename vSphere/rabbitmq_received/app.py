from flask import Flask, jsonify, request
import pika

app = Flask(__name__)

#Display vDesks from Searched User
@app.route("/message", methods=['GET'])
def get_message():
  parameters = pika.ConnectionParameters(host='localhost')
  connection = pika.BlockingConnection(parameters)
  channel = connection.channel()
  channel.queue_declare(queue='vsphere1')
  method_frame, header_frame, body = channel.basic_get(queue='vsphere1')
  if method_frame:
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    #TO DO Call Jenkins Remote Trigger
    
    return 'Message'
  else:
    return 'No Message'

if __name__ == '__main__':
    app.run( port=5001)


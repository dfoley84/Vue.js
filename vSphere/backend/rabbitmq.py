import pika, json

def RabbitMQ_Sender(message):
    #Pass Information to RabbitMQ For Jenkins Jobs
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='vSphere', durable=False)
    channel.basic_publish(
        exchange='',
        routing_key='vSphere',
        body=json.dumps(message),
        properties=pika.BasicProperties(
        delivery_mode=2,
    ))
    connection.close()

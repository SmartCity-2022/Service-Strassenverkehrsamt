import pika
import sys
import configparser


configParser = configparser.RawConfigParser()
configPath = r'./config/config.cfg'
configParser.read(configPath)


def send(key=str, headers=list, properties=pika.spec.BasicProperties, payload=bytes):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(configParser.get("rabbitMQ-configuration", "HOST")))
    channel = connection.channel()

    channel.exchange_declare(exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), exchange_type='topic')

    routing_key = key
    channel.basic_publish(
        exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), properties=properties, routing_key=routing_key, body=payload)
    print(" [x] Sent %r:%r" % (routing_key, payload))
    connection.close()
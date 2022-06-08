import pika
import sys
import configparser


configParser = configparser.RawConfigParser()
configPath = r'./config/config.cfg'
configParser.read(configPath)


def send(key=str, headers=list, properties=pika.spec.BasicProperties, payload=bytes):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=configParser["rabbitMQ-configuration"]["host"],
            port=configParser["rabbitMQ-configuration"]["port"],
            credentials=pika.PlainCredentials(
                configParser["rabbitMQ-configuration"]["user"],
                configParser["rabbitMQ-configuration"]["password"]
            )
        )
    )
    channel = connection.channel()

    channel.exchange_declare(exchange=configParser.get("rabbitMQ-configuration", "exchange"), exchange_type='topic', durable=True)

    routing_key = key
    channel.basic_publish(
        exchange=configParser.get("rabbitMQ-configuration", "exchange"), properties=properties, routing_key=routing_key, body=payload)
    print(" [x] Sent %r:%r" % (routing_key, payload))
    connection.close()
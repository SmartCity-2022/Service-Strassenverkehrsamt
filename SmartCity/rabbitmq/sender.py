import pika
import sys
import configparser

configParser = configparser.RawConfigParser()
configPath = r'./config/config.cfg'
configParser.read(configPath)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(configParser.get("rabbitMQ-configuration", "HOST")))
channel = connection.channel()

channel.exchange_declare(exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), exchange_type='topic')

routing_key = configParser.get("rabbitMQ-configuration", "ROUTING_KEY")
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
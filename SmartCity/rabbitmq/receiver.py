import pika
import sys
import configparser
import threading

class MQReceiver(threading.Thread):
    
    
    def run(self):
        configParser = configparser.RawConfigParser()
        configPath = r'./config/config.cfg'
        configParser.read(configPath)
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=configParser.get("rabbitMQ-configuration", "HOST")))
        channel = connection.channel()
        channel.exchange_declare(exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), exchange_type='topic')

        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(
                exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), queue=queue_name, routing_key="*.#")

        print(' [*] Waiting for Events. To exit press CTRL+C')
        
        def callback(ch, method, properties, body):
            print(" ---Event received--- \n")
            print(f" [x] Routing Key: {method.routing_key}")
            print(f" [x] Message: {body}", "\n\n\n")    
            
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
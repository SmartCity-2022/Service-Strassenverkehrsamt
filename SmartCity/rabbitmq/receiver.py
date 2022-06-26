import pika
import sys
import configparser
import threading
import api.jwt

class MQReceiver(threading.Thread):
    
    
    def run(self):
        configParser = configparser.RawConfigParser()
        configPath = r'./config/config.cfg'
        configParser.read(configPath)
        try:
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
        except:
            return
        channel = connection.channel()
        channel.exchange_declare(exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), exchange_type='topic', durable=True)

        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(
                exchange=configParser.get("rabbitMQ-configuration", "EXCHANGE"), queue=queue_name, routing_key="*.#")

        print(' [*] Waiting for Events. To exit press CTRL+C')
        
        def callback(ch, method, properties, body):
            body = str(body)[2:len(str(body))-1]
            print(" ---Event received--- ")
            print(f" [x] Routing Key: {method.routing_key}")
            print(f" [x] Message: {body}", "\n")    
            if method.routing_key == configParser.get("rabbitMQ-routes", "WORLD"):
                api.jwt.JWT_SECRET = str(body)
            
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
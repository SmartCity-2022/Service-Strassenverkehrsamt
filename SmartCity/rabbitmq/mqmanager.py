from rabbitmq.receiver import MQReceiver
from rabbitmq.sender import send
import time
import pika
import threading
import configparser
import sys

class MQManager(threading.Thread):


    def __init__(self):
        super().__init__()
        self.retry_delay = 5
        self.retries = 0
        self.success = False
        self.receiver = MQReceiver()
        self.receiver.daemon = True
        self.configParser = configparser.RawConfigParser()
        self.configPath = r'./config/config.cfg'
        self.configParser.read(self.configPath)
    
    
    def run(self):
        
        if not self.success:
            try:
                self.receiver.start()
                send(key=self.configParser.get("rabbitMQ-routes", "HELLO"), headers=None, properties=None, payload="")
                self.success = True
                return
            except:
                self.retries +=1
                print(f" [x] Could not establish connection to RabbitMQ host after {self.retries} tries.", "\n")  
                print(f" [x] Retrying in {self.retry_delay} seconds.", "\n") 
                time.sleep(self.retry_delay)
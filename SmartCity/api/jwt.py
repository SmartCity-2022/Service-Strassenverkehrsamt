import jwt
import configparser
import datetime


configParser = configparser.RawConfigParser()
configPath = r'./config/config.cfg'
configParser.read(configPath)
jwtSecret = configParser["jwt-secret"]["SECRET"]


def encode_token(token=str):
    return jwt.decode(token, jwtSecret, algorithms=["HS256"])


def verify(timestamp = datetime.datetime):
    if timestamp > datetime.datetime.now():
        return True
    return False
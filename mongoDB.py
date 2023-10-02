import pymongo
import sys
import ssl
from os import environ as env

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


try:
    host = env["MONGO_CONNECT_TOKEN"]
except KeyError:
    print('[error]: `MONGO_CONNECT_TOKEN` environment variable required')
    sys.exit(1)

def connect():
    client = MongoClient(host, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
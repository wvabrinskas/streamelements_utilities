import requests
import json

def payload(state):
    return { 'enabled' : state }

def headers():
    config = readConfig()
    authToken = config["jwt-token"]
    return { "Authorization" : "Bearer " + authToken }

def readConfig():
    with open('../config.json') as config_file:
            return json.load(config_file)

def url(): 
    return "https://api.streamelements.com/kappa/v2/songrequest/" + readConfig()["channel"] + "/settings"

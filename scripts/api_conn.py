import http.client
import json

conn = http.client.HTTPConnection('127.0.0.1:3002')

headers = {'Content-type': 'application/json'}



def SendMessage(msg:str):
    foo = {
        "message": msg,
    }

    json_data = json.dumps(foo)

    conn.request('POST', '/conversation', json_data, headers)

    response = conn.getresponse()
    textRes = json.loads(response.read())
    return textRes

def SendMessages(messages:list):
    context = ""
    for msg in messages:
        context+=msg["content"]
    foo = {
        "message": context,
    }

    json_data = json.dumps(foo)

    conn.request('POST', '/conversation', json_data, headers)

    response = conn.getresponse()
    textRes = json.loads(response.read())
    return textRes

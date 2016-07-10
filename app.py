from flask import Flask
import json
import time
import paho.mqtt.client as mqtt
creds = {
    'clientId': 'TT2DMJUPgQIeeHudUeT9UPg',
    'user':     '4f60cc25-43e0-4087-9e1e-e754793f543e',
    'password': 'j5u0sR_NvnEq',
    'topic':    '/v1/4f60cc25-43e0-4087-9e1e-e754793f543e/',
    'server':   'mqtt.relayr.io',
    'port':     1883
}
# ATTENTION !!!
# DO NOT try to set values under 200 ms of the server
# will kick you out
publishing_period = 1000
app = Flask(__name__)

@app.route("/")
#def hello():
    #return "Hello World!!"

self.client = client
self.credentials = creds

    def on_connect(self, client, userdata, flags, rc):
        return "Connected."
        # self.client.subscribe(self.credentials['topic'].encode('utf-8'))
        self.client.subscribe(self.credentials['topic'] + 'cmd')

    def on_message(self, client, userdata, msg):
        return "Command received: %s' % msg.payload"

    def on_publish(self, client, userdata, mid):
        return "Message published."


def main(creds, publishing_period):
    client = mqtt.Client(client_id=credentials['clientId'])
    delegate = MqttDelegate(client)
    client.on_connect = delegate.on_connect
    client.on_message = delegate.on_message
    client.on_publish = delegate.on_publish
    user, password = credentials['user'], credentials['password']
    client.username_pw_set(user, password)
    # client.tls_set(cafile)
    # client.tls_insecure_set(False)
    try:
        return "Connecting to mqtt server."
        server, port = credentials['server'], credentials['port']
        client.connect(server, port=port, keepalive=60)
    except:
        return "Connection failed, check your credentials!"
        

    # set 200 ms as minimum publishing period
    if publishing_period < 200:
        publishing_period = 200

    while True:
        client.loop()

        # publish data
        message = {
            'meaning': 'someMeaning',
            'value': 'py something'
        }
        client.publish(credentials['topic'] +'data', json.dumps(message))

        time.sleep(publishing_period / 1000.)



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

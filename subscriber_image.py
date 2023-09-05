import paho.mqtt.client as mqtt

import json
import time
import classify_image_custom as image_classify

# Client Name
CLIENT_NAME = 'IoT'
# Broker IP
HOST_NAME = 'circular.polito.it'


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
	print("Connected to broker with result code {0}".format(str(rc)))  # Print result of connection attempt
	client.subscribe('#')

def on_message(client, userdata, message):
    print("Message received.")
    image_classify.mqtt_classify(message.payload)
	


if __name__ == '__main__':

	mqttClient = mqtt.Client(CLIENT_NAME)
	mqttClient.on_connect = on_connect
	mqttClient.on_message = on_message
	mqttClient.tls_set(ca_certs="/home/fvolante/ca.crt")

	mqttClient.tls_insecure_set(True)
	mqttClient.connect(HOST_NAME, port=8883)
	mqttClient.loop_forever()

	
	


import paho.mqtt.client as mqtt

import json
import time
import classify_image_custom as image_classify

# Client Name
CLIENT_NAME = 'IoT'
# Broker IP
HOST_NAME = 'circular.polito.it'
# Output host IP
OUTPUT_HOST_NAME = 'test.mosquitto.org'

clients = []

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
	print("Connected to broker with result code {0}".format(str(rc)))  # Print result of connection attempt
	client.subscribe('#')

def on_connect_resp(client, userdata, flags, rc):  # The callback for when the client connects to the broker
	print("Connected to broker with result code {0}".format(str(rc)))

def on_message(client, userdata, message):
    print("Message received.")
    image_classify.mqtt_classify(message.payload)
    clients[1].publish("/fvolante/output", "work done")
    time.sleep(1)
    print("Done")
    
	


if __name__ == '__main__':

	mqttClient = mqtt.Client(CLIENT_NAME)
	mqttClient.on_connect = on_connect
	mqttClient.on_message = on_message
	mqttClient.tls_set(ca_certs="/home/fvolante/ca.crt")
	mqttClient.tls_insecure_set(True)
	mqttClient.connect(HOST_NAME, port=8883)
	ret_client =mqtt.Client(CLIENT_NAME)
	ret_client.on_connect = on_connect_resp
	ret_client.connect(OUTPUT_HOST_NAME, port=1883)
	clients.append(mqttClient)
	clients.append(ret_client)
	while(True):
		for client in clients:
			client.loop(0.1)
		

	
	

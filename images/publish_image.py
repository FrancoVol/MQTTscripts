import paho.mqtt.client as mqtt
import time

#####IMPORTANT: RUN USING PYTHON3, DOES NOT WORK WITH PYTHON2 DUE TO THE FACT THAT PAHO MQTT ONLY SENDS STRINGS
#####			FOR SOME REASON, AND IN THIS EXAMPLE THERE IS THE NEED TO SEND A BYTEARRAY
##### IMPORTANT2: THE SLEEPS ARE NECESARY TO FIRSTLY CONNECT CORRECTLY TO THE BROKER, THEN TO WAIT THAT ALL THE DATA
##### 			  IS SENT BEFORE CLOSING THE CONNECTION
# Broker IP
HOST_NAME = 'circular.polito.it'
# client name
CLIENT_NAME = 'test'

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
	print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
	
if __name__ == '__main__':
	client =mqtt.Client(CLIENT_NAME)
	client.on_connect = on_connect

	client.tls_set(ca_certs="/home/francovolante/Desktop/certs/ca.crt")	
	client.tls_insecure_set(True)
	client.connect(HOST_NAME, port=8883)
	
	client.loop_start()
	time.sleep(2)

	with open('parrot.jpg', 'rb') as file:
		file_content = file.read()
		msg = bytearray(file_content)
		result = client.publish("image/", msg)
		msg_status = result[0]
		if msg_status == 0:
			print("Message sent correctly")
		else:
			print("Error in sending the message")
	time.sleep(2)
	client.loop_stop()

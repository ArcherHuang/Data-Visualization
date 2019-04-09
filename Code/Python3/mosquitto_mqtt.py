# pip install paho-mqtt

import paho.mqtt.client as mqtt
import time
import json
import random

# *********************************************************************
# MQTT Config

dataChnId1 = "Temperature"
dataChnId2 = "Humidity"
MQTT_SERVER = "52.206.47.47"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC1 = "mosquitto/" + dataChnId1
MQTT_TOPIC2 = "mosquitto/" + dataChnId2

# *********************************************************************

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)	

while True:
  h0 = random.randint(0,30)
  t0 = random.randint(0,30)
  payload = {"dataChnId":dataChnId1,"value":t0}
  print(dataChnId1 + " : " + str(t0))
  mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
  payload = {"dataChnId":dataChnId2,"value":h0}
  print(dataChnId2 + " : " + str(h0))
  mqtt_client.publish(MQTT_TOPIC2, json.dumps(payload), qos=1)
  time.sleep(10)
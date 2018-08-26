import paho.mqtt.client as mqttClient
import time

################
import urllib.request
import requests
import json
# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
user = "publish"
password = "publish"
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "Area1/Zone1"

broker_address= "localhost"
port = 1883

import time
timestamp = int(time.time())

#url = "https://api.myjson.com/bins/1ak7li"
#url = "http://services.groupkt.com/state/get/IND/all"

url = "http://192.168.1.102/smarttablechart/ignition_group1.php"

#response = urllib.request.urlopen(url)
#data = json.loads(response.read())
response = requests.get(url)
data = response.json()
print ("url connected1...")
MQTT_MSG=json.dumps(data);
#########

 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker... will autopublish every 10secs")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
Connected = False   #global variable for the state of the connection


client = mqttClient.Client("Python", protocol=mqttClient.MQTTv311)               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(1)
 
try:
    while True:
        time.sleep(4)
#        value = input('Enter to continue:')
        client.publish("Area1/test", MQTT_MSG)

        url = "http://192.168.1.102/smarttablechart/ignition_group1.php"

        response = requests.get(url)
        data = response.json()
        MQTT_MSG=json.dumps(data);
        print ("published...")

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()


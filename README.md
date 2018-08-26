# IgitionMQTTClient
Let's build an MQTT client module for Ignition

Tested on Ubuntu 18.04, openjdk version "1.8.0_181"

![](https://github.com/alamsha/IgitionMQTTClient/blob/master/images/EMQ-dashboard.png)
**Make sure all these ports are visible. If not, may be another broker like Mosquitto, Mosca etc is running. Stop it and restart emqttd.**


**Step 1 --- Setup EMQ(emqttd) Broker:**

Download and install the latest stable deb version from this site:

Make sure no other MQTT brokers like Moquitto, Mosca etc is running to avoid port clash.

Start emdttd broker:

    sudo systemctl status emqttd.service
        

Launch the EMQ Admin Dashboard:

http://localhost:18083/#/listeners

user: admin

password: public

http://emqtt.io/downloads



**Step 2 --- Download this repo:**

    cd mqtt-ignition/
    


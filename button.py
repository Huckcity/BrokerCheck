from gpiozero import LED, Button
from signal import pause
import adalcd as lcd
import subprocess
import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

lcd.print("Welcome!")
time.sleep(3)
lcd.clear()
lcd.print("Connecting...")
time.sleep(2)
lcd.clear()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)

    else:
        print("Bad connection Returned code=", rc)

# def on_subscribe(client, userdata, mid, granted_qos):

def on_message(client, userdata, msg):
    lcd.printout("STORED MESSAGES: "+msg.payload.decode('utf-8'))
    mqttc.unsubscribe("$SYS/broker/messages/stored")
    lcd.clear()

client_id = f'python-mqtt-{random.randint(0, 1000)}'
mqttc = mqtt.Client(client_id, clean_session=True,
                    userdata=None, transport="websockets")

mqttc.on_connect = on_connect
# mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

mqttc.tls_set()
mqttc.connect('mqtt.huckcity.ie', 9001)
mqttc.loop_start()

led = LED(17)
button = Button(27)

led.source = button

lcd.cursor = True
lcd.blink = True

def onFunc():
    lcd.clear()
    mqttc.subscribe("$SYS/broker/messages/stored", 2)


button.when_pressed = onFunc

pause()

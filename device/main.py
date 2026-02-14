# Imports
import time
import json
import random
import math
import paho.mqtt.client as mqtt
from datetime import datetime

# MQTT Configuration'
BROKER_HOST = "test.mosquitto.org"
BROKER_PORT = 1883
DEVICE_ID = "vdev-001"
TOPIC_PUB = f"iot/{DEVICE_ID}/telemetry"
TOPIC_SUB = f"iot/{DEVICE_ID}/command"

# Virtual Hardware State
class VirtualDevice:
    def __init__ (self):
        self.led_state = False
        self.temperature = 22.0 # Starting Temp (Celsius)
        self.humidity = 45.0 # Starting Humidity (%)
        self.fan_status = "OFF"

    def update_physic (self):
        # Simulate Environmental Physic Changes

        noise = random.uniform(-0.1, 0.1)

        if self.led_state:
            self.temperature += 0.5 + noise # LED ON increases temperature, Heat Up.
        elif self.fan_status == "ON":
            self.temperature -= 0.3 + noise # Fan ON decreases temperature, Cool Down.
        else:
            self.temperature += (math.sin(time.time() / 10) * 0.1) + noise # Natural Fluctuation Waves

        # Clampo Humidity Increase to Temperature (Roughly)
        self.humidity = max (30, min (90, self.humidity + random.uniform (-0.5, 0.5)))
        self.temperature = round (self.temperature, 2)
        self.humidity = round (self.humidity, 2)

device = VirtualDevice() # Instantiate Virtual Device

# MQTT Handlers

def on_connect (client, userdata, flags, rc): # MQTT Connection Handler
    if rc == 0:
        print (f"[SYSTEM] Connected to Broker. Subscribing to {TOPIC_SUB}")
        client.subscribe (TOPIC_SUB)
    else:
        print (f"[ERROR] Connection Failed. Code: {rc}")

def on_message (client, userdata, msg): # MQTT Message Handler
    try:
        # Parse Incoming Command
        payload = json.loads (msg.payload.decode())
        print (f"[CMD] Recieved: {payload}")

        # Handle Actuator Commands
        if "led" in payload: # LED Command
            device.led_state = bool (payload ["led"])
            print (f"[ACTUATOR] LED switch {'ON' if device.led_state else 'OFF'}")

        if "fan" in payload: # Fan Command
            device.fan_status = "ON" if payload ["fan"] else "OFF"
            print (f"[ACTUATOR] Fan switch {device.fan_status}")

    except Exception as e: # Handle Parsing Errors
        print (f"[ERROR] Failed to Parse Command: {e}")

# MQTT Loop

# MQTT Client Setup
# client = mqtt.Client() # Create MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2) # Create MQTT Client (with API v2)
client.on_connect = on_connect # Set Connection Handler
client.on_message = on_message # Set Message Handler

print (f"[SYSTEM] Initializing Virtual IoT Device...")

try:
    client.connect (BROKER_HOST, BROKER_PORT, 60) # Connect to MQTT Broker
    client.loop_start() # Start MQTT Loop

    while True:
        device.update_physics() # Update Physics
        telemetry = { # Prepare JSON Payload
            "device_id": DEVICE_ID,
            "timestamp": datetime.now().isoformat(),
            "sensors": { # Sensor Readings
                "temperature": device.temperature,
                "humidity": device.humidity
            },
            "status": { # Actuator Status
                "led": device.led_state,
                "fan": device.fan_status
            }
        }

        # Publish
        client.publish (TOPIC_PUB, json.dumps (telemetry)) # Publish Telemetry
        print (f"[TX] Sent: {telemetry['sensors']} | LED: {telemetry['status']['led']}")

        time.sleep (2) # Delay Between Telemetry Updates (Sleep)

except KeyboardInterrupt: # Graceful Shutdown on Ctrl+C
    print ("\n[SYSTEM] Shutting Down Virtual Device...")
    client.loop_stop() # Stop MQTT Loop
    client.disconnect() # Disconnect from Broker
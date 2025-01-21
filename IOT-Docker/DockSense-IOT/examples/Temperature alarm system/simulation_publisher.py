import random
import time
import json
import paho.mqtt.client as mqtt

broker = "localhost"  # Match the working `mosquitto_pub` address
port = 1884
topic = "test/topic"  # Ensure this matches the subscription topic

client = mqtt.Client(protocol=mqtt.MQTTv311)

# Connect to the broker
try:
    client.connect(broker, port, 60)
    print(f"Connected to MQTT broker at {broker}:{port}")
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

client.loop_start()

try:
    while True:
        # Simulate a temperature reading
        temperature = random.uniform(20.0, 100.0)
        cpu_usage = random.uniform(10.0, 90.0)
        data = {"temperature": temperature, "cpu_usage": cpu_usage}
        
        # Publish to MQTT topic
        try:
            client.publish(topic, json.dumps(data))
            print(f"Published: {data}")
        except Exception as e:
            print(f"Error publishing message: {e}")
        
        time.sleep(5)
except KeyboardInterrupt:
    print("Simulation stopped by user.")

client.loop_stop()
client.disconnect()

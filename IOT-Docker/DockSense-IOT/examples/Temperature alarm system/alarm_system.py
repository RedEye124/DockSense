import json
import paho.mqtt.client as mqtt

broker = "localhost"  # Ensure this matches the working broker address
port = 1884
topic = "test/topic"  # Ensure this matches the topic being published
threshold = 75.0       # Temperature threshold for alarm

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    if rc == 0:
        print(f"Subscribed to topic: {topic}")
        client.subscribe(topic)
    else:
        print("Failed to connect to the broker.")

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload.decode())
        temperature = data.get("temperature", 0)
        print(f"Received temperature: {temperature}°C")
        if temperature > threshold:
            print("🚨 Alarm: High temperature detected! Triggering alarm system! 🚨")
    except Exception as e:
        print(f"Error processing message: {e}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(broker, port, 60)
    print(f"Connecting to broker at {broker}:{port}")
except Exception as e:
    print(f"Failed to connect to broker: {e}")
    exit(1)

client.loop_forever()

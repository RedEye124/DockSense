from prometheus_client import start_http_server, Gauge
import paho.mqtt.client as mqtt
import json

# Prometheus metrics
temperature_gauge = Gauge("iot_temperature", "Temperature readings from sensors", ["device_id"])
cpu_usage_gauge = Gauge("iot_cpu_usage", "CPU usage of devices", ["device_id"])

# MQTT settings
broker = "localhost"  # Replace with 'host.docker.internal' if on Windows/WSL
port = 1884
topic = "test/topic"  # Matches the publisher topic

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload.decode())
        device_id = "test_device"  # Use a default device ID for testing
        temperature = data.get("temperature")
        cpu_usage = data.get("cpu_usage")
        if temperature is not None:
            print(f"Updating temperature for {device_id}: {temperature}")
            temperature_gauge.labels(device_id=device_id).set(temperature)
        if cpu_usage is not None:
            print(f"Updating CPU usage for {device_id}: {cpu_usage}")
            cpu_usage_gauge.labels(device_id=device_id).set(cpu_usage)
    except Exception as e:
        print(f"Error processing message: {e}")
        

if __name__ == "__main__":
    start_http_server(9100)  # Prometheus will scrape metrics from this port
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(broker, port, 60)
        client.loop_forever()
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")

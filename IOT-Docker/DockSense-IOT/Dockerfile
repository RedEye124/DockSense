# Base image: Lightweight Python for running IoT services
FROM python:3.9-slim

# Install Mosquitto MQTT broker and client tools
RUN apt-get update && apt-get install -y --no-install-recommends \
        mosquitto \
        mosquitto-clients \
    && rm -rf /var/lib/apt/lists/*

# Copy the Mosquitto configuration into the container
COPY mosquitto.conf /etc/mosquitto/mosquitto.conf

# Set the working directory for DockSense
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the MQTT broker port
EXPOSE 1884

# Start Mosquitto broker when the container starts
CMD ["sh", "-c", "mosquitto -c /etc/mosquitto/mosquitto.conf -v"]

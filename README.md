# DockSense: Lightweight IoT Simulation and Monitoring Framework

DockSense is a lightweight, open-source framework designed to simplify IoT device simulation and performance monitoring. It provides a pre-configured environment for MQTT messaging, real-time metrics collection, and interactive dashboards, making it ideal for testing IoT applications without the need for physical hardware.

## Features
-  Pre-configured MQTT broker.
-  Integrated Prometheus metrics.
-  Intuitive Grafana dashboards.

## Lets Get Started 
Follow these steps to set up and run DockSense. After completing these steps, you will have access to tools for simulating IoT devices, visualizing real-time metrics in Grafana, and monitoring system performance using Prometheus. This allows you to test IoT applications and scenarios effectively without requiring physical hardware. 

### Step 1: Clone the Repository
`git clone https://github.com/RedEye124/DockSense.git
cd DockSense`

### Step 2: Build the Docker Image
`docker build -t ns6819/docksense`

### Step 3: Start the Docker Compose Stack
`docker-compose up `

### Step 4: Access the Services

- Grafana Dashboard: http://localhost:3000(Default credentials: admin / admin)

- Prometheus Metrics: http://localhost:9090

- Metrics Exporter: http://localhost:9100/metrics

##  Simulating IoT Devices

I provided  a sample example or Temperature based alarm system python codes in the github repository under examples folder after executing the steps above you can run this codes this will helps us to understand more how this project  actually works

### Step 1. Open a new WSL terminal check the containers running you will find a container which is running dockerscence image copy the conainer id.
`docker ps`

`docker exec -it < conainer-id-of-dockerscence image > bash`
example
`docker exec -it a2c bash`

### Step 2.  Subscribe to MQTT Topics
`mosquitto_sub -h localhost -p 1884 -t "test/topic" -v`

### Step 3. Open a New wsl terminal and run this will publish a message to the subscriber
`mosquitto_pub -h localhost -p 1884 -t "test/topic" -m "Hello MQTT"`

If you see Hello MQTT message in the container it means your mqtt connection is working now its time to test it on an iot simulation . open folder provided in github.

### Step 1:  Repeat previous steps 1 and 2.

### step 2: open the folder example and temperature in 2 differetn terminals  and run 

`python simulation_publisher.py` 
`python alarm_system.py`
in each terminal 

### Step 3: Open a new terminal and check if there is a file mqtt_expoter.py and Run 
`python mqtt_exporter.py`

By following this steps you will find  simulation_publisher.py generates random temperature and cpu values and send it to the contianer and the alarm_system will see if there is any temperature value above 75 and triggers a warning . The mqtt_exporter will read the values and send it to the promateus so we can create dashboards in grafana.


## If you face any issues will running the conauners like port already in use like that run 
`sudo lsof -I :poet number`
`sudo kill - pid`




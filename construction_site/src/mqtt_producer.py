import paho.mqtt.client as mqtt
import json


class mqtt_publisher:
    def __init__(self, address, port, clientID) -> None:
        self.mqttBroker = address
        self.port = port
        self.clientID = clientID
        self.client = None
    
    def connect_client(self):
        MQTT_KEEPALIVE_INTERVAL = 45
        self.client = mqtt.Client(self.clientID)
        self.client.connect(host=self.mqttBroker, port=self.port, keepalive=MQTT_KEEPALIVE_INTERVAL)

    def connect_client_secure(self, username, password):
        MQTT_KEEPALIVE_INTERVAL = 60
        self.client = mqtt.Client(self.clientID)
        self.client.username_pw_set(username=username, password=password)
        self.client.tls_set()  # Uses TLS for a secure connection
        self.client.connect(host=self.mqttBroker, port=self.port, keepalive=MQTT_KEEPALIVE_INTERVAL)

    def publish_to_topic(self, topic: str, speed, temperature, vibration):
        payload = {
            "speed": speed,
            "temperature": temperature,
            "vibration": vibration
        }
        result = self.client.publish(topic, json.dumps(payload))
        status = result[0]
        if status == 0:
            print(f"Successfully published to topic {topic} with payload {payload}")
        else:
            print(f"Failed to publish message to topic {topic}")

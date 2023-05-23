import json
import random
import time
import datetime
import uuid
from dataclasses import field, dataclass

from kafka import KafkaProducer

TOPIC_NAME = "kafka_blog"


@dataclass
class SensorEvent:
    """Sensor template event"""
    sensor_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    temperature: float = field(default_factory=lambda: random.uniform(20.0, 37.5))
    humidity: float = field(default_factory=lambda: random.uniform(33.0, 49.9))
    timestamp: datetime = field(default_factory=lambda: datetime.datetime.now().isoformat())

    def to_json(self):
        return json.dumps(self.__dict__)


producer = KafkaProducer(
    bootstrap_servers=f"kafka-aa80066-kafka-blog.aivencloud.com:14640",
    security_protocol="SSL",
    ssl_cafile="cert/ca.pem",
    ssl_certfile="cert/service.cert",
    ssl_keyfile="cert/service.key",
)

for _ in range(100):
    message = SensorEvent().to_json()
    producer.send(TOPIC_NAME, message.encode('utf-8'))
    print(f"Message sent: {message}")
    time.sleep(1)

producer.close()

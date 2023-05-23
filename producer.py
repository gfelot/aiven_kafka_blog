import time
import datetime
from kafka import KafkaProducer

TOPIC_NAME = "demo_blog"

event = {
    "sensor_id": "sensor-001",
    "temperature": 25.5,
    "humidity": 60.2,
    "timestamp": datetime.datetime.now().isoformat()
}

producer = KafkaProducer(
    bootstrap_servers=f"kafka-25bd5837-kafka-blog.aivencloud.com:14640",
    security_protocol="SSL",
    ssl_cafile="cert/ca.pem",
    ssl_certfile="cert/service.cert",
    ssl_keyfile="cert/service.key",
)

for i in range(100):
    message = f"Hello from Python using SSL {i + 1}!"
    producer.send(TOPIC_NAME, message.encode('utf-8'))
    print(f"Message sent: {message}")
    time.sleep(1)

producer.close()

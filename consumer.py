from kafka import KafkaConsumer

TOPIC_NAME = "demo_blog"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=f"kafka-25bd5837-kafka-blog.aivencloud.com:14640",
    client_id = "CONSUMER_CLIENT_ID",
    group_id = "CONSUMER_GROUP_ID",
    security_protocol="SSL",
    ssl_cafile="cert/ca.pem",
    ssl_certfile="cert/service.cert",
    ssl_keyfile="cert/service.key",
)

while True:
    for message in consumer.poll().values():
        print("Got message using SSL: " + message[0].value.decode('utf-8'))

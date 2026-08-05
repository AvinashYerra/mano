from kafka import KafkaProducer
import json

from shared.config import settings


class Producer:

    def __init__(self):

        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def publish(self, topic: str, message: dict):

        self.producer.send(topic, message)
        self.producer.flush()

        print(f"[Producer] {topic}")
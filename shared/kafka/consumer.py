from kafka import KafkaConsumer
import json

from shared.config import settings


class Consumer:

    def __init__(self, topic, group_id=None):

        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            group_id=group_id,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

    def listen(self):

        for message in self.consumer:
            yield message.value
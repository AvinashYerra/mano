from shared.kafka.producer import Producer
from shared.kafka.consumer import Consumer
from shared.kafka.topics import AUDIO_TOPIC

import threading
import time


def consume():

    consumer = Consumer(
        AUDIO_TOPIC,
        group_id="test-consumer"
    )

    print("Listening...")

    for message in consumer.listen():
        print(message)


threading.Thread(target=consume, daemon=True).start()

time.sleep(2)

producer = Producer()

producer.publish(
    AUDIO_TOPIC,
    {
        "session_id": "001",
        "audio_chunk": "Hello Kafka",
        "timestamp": "2026-08-02"
    }
)

time.sleep(5)
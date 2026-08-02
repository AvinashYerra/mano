from kafka import KafkaProducer
import json
import time


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


messages = [
    {
        "session_id": "test-001",
        "audio_chunk": "hello world",
        "timestamp": "2026-08-02T20:00:00"
    },
    {
        "session_id": "test-002",
        "audio_chunk": "testing kafka pipeline",
        "timestamp": "2026-08-02T20:01:00"
    }
]


for message in messages:

    producer.send(
        "audio.raw.v1",
        message
    )

    print("Sent:", message)

    time.sleep(1)


producer.flush()

print("Producer completed")
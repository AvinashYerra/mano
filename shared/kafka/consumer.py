from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    "audio.raw.v1",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


print("Consumer started...")


for message in consumer:

    print("\nReceived message:")
    print(message.value)
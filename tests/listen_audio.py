from shared.config import settings
from shared.kafka.consumer import Consumer
from shared.kafka.topics import AUDIO_TOPIC

print("Bootstrap:", settings.KAFKA_BOOTSTRAP_SERVERS)
print("Topic:", AUDIO_TOPIC)

consumer = Consumer(
    AUDIO_TOPIC,
    group_id="audio-listener-v2"   # use a new group
)

print("Listening...")

for message in consumer.listen():
    print(message)
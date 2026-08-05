from datetime import datetime

from shared.kafka.producer import Producer
from shared.kafka.topics import AUDIO_TOPIC


class AudioPublisher:

    def __init__(self):

        self.producer = Producer()

    def publish(self, session_id, chunk):

        message = {
            "session_id": session_id,
            "chunk_id": chunk["chunk_id"],
            "audio_chunk": chunk["text"],
            "timestamp": datetime.utcnow().isoformat()
        }

        self.producer.publish(
            AUDIO_TOPIC,
            message
        )
from kafka.admin import KafkaAdminClient, NewTopic

TOPICS = [
    "audio.raw.v1",
    "transcript.v1",
    "gloss.v1",
    "animation.instructions.v1",
    "metrics.v1",
    "deadletter.v1",
]

admin = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="accessibility-platform",
)

existing = admin.list_topics()

new_topics = []

for topic in TOPICS:

    if topic not in existing:

        new_topics.append(
            NewTopic(
                name=topic,
                num_partitions=3,
                replication_factor=1,
            )
        )

if new_topics:
    admin.create_topics(new_topics)

print("Topics created successfully.")
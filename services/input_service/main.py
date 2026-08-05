import uuid

from services.input_service.chunker import Chunker
from services.input_service.publisher import AudioPublisher


INPUT_FILE = "storage/audio_chunks/sample.txt"


def main():

    session_id = str(uuid.uuid4())

    print(f"Session : {session_id}")

    chunker = Chunker()

    publisher = AudioPublisher()

    chunks = chunker.chunk(INPUT_FILE)

    print(f"Generated {len(chunks)} chunks")

    for chunk in chunks:

        publisher.publish(
            session_id,
            chunk
        )

        print(f"Published chunk {chunk['chunk_id']}")

    print("Input Service Finished")


if __name__ == "__main__":

    main()
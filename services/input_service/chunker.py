from pathlib import Path


class Chunker:

    def chunk(self, input_file):

        chunks = []

        with open(input_file, "r") as f:

            for index, line in enumerate(f):

                chunks.append(
                    {
                        "chunk_id": index,
                        "text": line.strip()
                    }
                )

        return chunks
from pydantic import BaseModel

from datetime import datetime


class AudioEvent(BaseModel):

    stream_id: str

    chunk_id: int

    audio_path: str

    timestamp: datetime

    duration_ms: int

    sample_rate: ints
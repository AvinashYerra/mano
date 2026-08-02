from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str

    LOG_LEVEL: str

    KAFKA_BOOTSTRAP_SERVERS: str

    KAFKA_AUDIO_TOPIC: str

    KAFKA_TRANSCRIPT_TOPIC: str

    KAFKA_GLOSS_TOPIC: str

    KAFKA_ANIMATION_TOPIC: str

    KAFKA_METRICS_TOPIC: str

    KAFKA_DLQ_TOPIC: str

    SPARK_APP_NAME: str

    SPARK_MASTER: str

    STREAMLIT_PORT: int

    STORAGE_DIR: str

    class Config:
        env_file = ".env"


settings = Settings()
# Root files
touch README.md LICENSE .gitignore .env.example requirements.txt docker-compose.yml

# Documentation
mkdir -p docs/images
touch docs/architecture.md
touch docs/checkpoints.md
touch docs/kafka-topics.md
touch docs/api-contracts.md
touch docs/deployment.md

# Assets
mkdir -p assets/signs/words
mkdir -p assets/signs/alphabet
mkdir -p assets/signs/phrases
mkdir -p assets/metadata
mkdir -p assets/sample_videos

touch assets/metadata/dictionary.json
touch assets/metadata/glossary.json

# Configs
mkdir -p configs/kafka
mkdir -p configs/spark
mkdir -p configs/logging
mkdir -p configs/streamlit

# Shared
mkdir -p shared/models
mkdir -p shared/kafka
mkdir -p shared/utils

touch shared/__init__.py
touch shared/config.py
touch shared/constants.py
touch shared/logger.py

touch shared/models/audio_event.py
touch shared/models/transcript_event.py
touch shared/models/gloss_event.py
touch shared/models/animation_event.py
touch shared/models/metrics_event.py

touch shared/kafka/producer.py
touch shared/kafka/consumer.py
touch shared/kafka/topics.py

touch shared/utils/file_utils.py
touch shared/utils/json_utils.py
touch shared/utils/audio_utils.py
touch shared/utils/time_utils.py

# Services
mkdir -p services/input_service
mkdir -p services/speech_service
mkdir -p services/gloss_service
mkdir -p services/dictionary_service
mkdir -p services/renderer_service
mkdir -p services/controller_service

touch services/input_service/main.py
touch services/input_service/downloader.py
touch services/input_service/extractor.py
touch services/input_service/chunker.py
touch services/input_service/producer.py
touch services/input_service/config.py

touch services/speech_service/main.py
touch services/speech_service/whisper_engine.py
touch services/speech_service/inference.py
touch services/speech_service/config.py

touch services/gloss_service/main.py
touch services/gloss_service/normalizer.py
touch services/gloss_service/translator.py
touch services/gloss_service/config.py

touch services/dictionary_service/main.py
touch services/dictionary_service/lookup.py
touch services/dictionary_service/redis_cache.py
touch services/dictionary_service/config.py

touch services/renderer_service/main.py
touch services/renderer_service/compositor.py
touch services/renderer_service/overlay.py
touch services/renderer_service/config.py

touch services/controller_service/main.py
touch services/controller_service/routes.py
touch services/controller_service/health.py
touch services/controller_service/config.py

# Spark
mkdir -p spark

touch spark/streaming_job.py
touch spark/state_manager.py
touch spark/metrics.py
touch spark/Dockerfile

# Dashboard
mkdir -p dashboard/pages
mkdir -p dashboard/components

touch dashboard/app.py

touch dashboard/pages/1_System_Status.py
touch dashboard/pages/2_Kafka_Metrics.py
touch dashboard/pages/3_Stream_Status.py
touch dashboard/pages/4_Dictionary.py
touch dashboard/pages/5_Latency.py

touch dashboard/components/cards.py
touch dashboard/components/charts.py
touch dashboard/components/tables.py

# Storage
mkdir -p storage/audio_chunks
mkdir -p storage/rendered
mkdir -p storage/downloads
mkdir -p storage/temp

# Scripts
mkdir -p scripts

touch scripts/setup.sh
touch scripts/run_services.sh
touch scripts/create_topics.py
touch scripts/reset_environment.sh

# Tests
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/sample_data

# Notebooks
mkdir -p notebooks

touch notebooks/dictionary_experiments.ipynb
touch notebooks/speech_experiments.ipynb

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

STORAGE_DIR = PROJECT_ROOT / "storage"

DOWNLOAD_DIR = STORAGE_DIR / "downloads"

AUDIO_DIR = STORAGE_DIR / "audio_chunks"

RENDER_DIR = STORAGE_DIR / "rendered"

TEMP_DIR = STORAGE_DIR / "temp"

ASSETS_DIR = PROJECT_ROOT / "assets"

SIGNS_DIR = ASSETS_DIR / "signs"

ALPHABET_DIR = SIGNS_DIR / "alphabet"

WORDS_DIR = SIGNS_DIR / "words"
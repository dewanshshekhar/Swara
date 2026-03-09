"""
ACE Studio Streamlit Configuration
"""
import os
import sys
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
EMPATH_ROOT = PROJECT_ROOT.parent.parent.parent  # Empath-1.5 repo root
CHECKPOINTS_DIR = EMPATH_ROOT / "checkpoints"
PROJECTS_DIR = PROJECT_ROOT / "projects"
OUTPUT_DIR = EMPATH_ROOT / "gradio_outputs"
CACHE_DIR = PROJECT_ROOT / ".cache"

# Ensure Empath repo is on Python path
if str(EMPATH_ROOT) not in sys.path:
    sys.path.insert(0, str(EMPATH_ROOT))

# Ensure directories exist
PROJECTS_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# UI Configuration
GENERATION_MODES = {
    "text2music": "🎵 Text to Music",
    "cover": "🎤 Create Cover",
    "repaint": "🎨 Repaint Section",
    "complete": "🎼 Complete Section",
    "extract": "🎹 Extract Vocals",
}

GENRES = [
    "Pop", "Hip-Hop", "Jazz", "Rock", "Classical",
    "Electronic", "Indie", "Country", "R&B", "Ambient"
]

MOODS = ["Energetic", "Chill", "Melancholic", "Uplifting", "Dark", "Dreamy"]

INSTRUMENTS = [
    "Guitar", "Piano", "Drums", "Bass", "Strings",
    "Synth", "Flute", "Trumpet", "Violin", "Cello"
]

# Generation defaults
DEFAULT_DURATION = 120  # seconds
DEFAULT_BPM = 120
DEFAULT_GUIDANCE = 7.5
DEFAULT_STEPS = 32  # Base model steps (turbo uses fewer)

# UI Display
SIDEBAR_ICON = "🎹"
APP_TITLE = "ACE Studio"
APP_SUBTITLE = "Music Generation & Editing"

# Supported audio formats
AUDIO_FORMATS = [".wav", ".mp3", ".m4a", ".flac"]

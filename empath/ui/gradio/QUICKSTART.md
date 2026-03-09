# 🎹 ACE Studio Streamlit MVP - Quick Start Guide

## ✅ What Was Created

A complete Streamlit UI for Empath v1.5 music generation with these features:

### 📁 Project Structure
```
empath/ui/streamlit/
├── main.py                 # Main Streamlit app (entry point)
├── config.py              # Configuration & constants
├── requirements.txt       # Python dependencies
├── README.md             # Full documentation
├── INSTALL.md            # Installation guide
├── run.sh / run.bat      # Quick start scripts
│
├── components/           # UI components
│   ├── dashboard.py      # Home with recent projects
│   ├── generation_wizard.py  # Create new songs
│   ├── editor.py         # Edit existing songs
│   ├── batch_generator.py   # Multi-song generation
│   ├── settings_panel.py    # Configuration
│   └── audio_player.py   # Audio playback
│
├── utils/                # Utility modules
│   ├── cache.py          # Model handler caching
│   ├── project_manager.py # Project save/load
│   └── audio_utils.py    # Audio file handling
│
└── projects/             # Auto-created: saved projects
```

## 🚀 Getting Started

### Option 1: Quick Start (Recommended)

```bash
cd empath/ui/streamlit
./run.sh  # macOS/Linux
# or
run.bat   # Windows
```

### Option 2: Manual Start

```bash
cd empath/ui/streamlit

# Install dependencies (one-time)
pip install -r requirements.txt

# Run the app
streamlit run main.py
```

The app will open at: **http://localhost:8501**

## 📋 Features Overview

### 🎵 Generate Tab
- **Step 1:** Choose genre/mood or describe your song
- **Step 2:** Set duration, BPM, key, lyrics
- **Step 3:** Fine-tune advanced settings
- Creates new project and saves metadata

### 🎛️ Edit Tab
- **Repaint:** Replace sections of audio
- **Cover:** Create cover versions
- **Extract:** Isolate vocals/stems
- **Complete:** Generate missing sections

### 📦 Batch Tab
- Queue up to 8 songs
- Batch generation with parallel processing
- See progress for each song
- Automatic project creation

### 📊 Dashboard Tab
- View recent projects with metadata
- Quick play/edit/delete buttons
- Project statistics
- One-click access to favorite songs

### ⚙️ Settings Tab
- Hardware info (GPU, CUDA, VRAM)
- Model selection and configuration
- Storage management and file cleanup
- Links to Empath resources

## 💾 Project Management

All generated songs are saved in `projects/` directory with:
- **Metadata** (genre, mood, BPM, duration, tags)
- **Audio files** (WAV format)
- **Creation/modification dates**

Projects can be:
- ✅ Played directly in UI
- ✅ Downloaded as WAV files
- ✅ Edited with advanced tools
- ✅ Deleted or renamed
- ✅ Tagged and organized

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Generation defaults
DEFAULT_DURATION = 120      # seconds
DEFAULT_BPM = 120
DEFAULT_GUIDANCE = 7.5
DEFAULT_STEPS = 32

# UI options
GENRES = ["Pop", "Hip-Hop", "Jazz", ...]
MOODS = ["Energetic", "Chill", ...]
INSTRUMENTS = ["Guitar", "Piano", ...]

# Storage
PROJECTS_DIR = "./projects"
CACHE_DIR = "./.cache"
```

## 🎮 Usage Workflow

1. **Start at Dashboard** → See all your songs
2. **Generate** → Create new song with wizard
3. **Edit** → Refine sections with editing tools
4. **Batch** → Generate multiple variations
5. **Settings** → Configure GPU/models as needed

## 📊 Architecture

```
Streamlit Frontend
  ↓
Session State Management
  ↓
Component Modules (Generation, Editor, etc.)
  ↓
Utility Layer (Project Manager, Audio Utils, Caching)
  ↓
Empath Handlers
  - AceStepHandler (DiT - Diffusion Transformer)
  - LLMHandler (Language Model for metadata)
  - DatasetHandler (Training data)
  ↓
PyTorch + CUDA/MPS/CPU
```

## 🔄 Integration with Empath

The Streamlit UI connects to Empath via:

1. **Handler Caching** (`utils/cache.py`)
   - Loads DIT and LLM handlers once
   - Persists across Streamlit reruns
   - Efficient VRAM usage

2. **Generation Parameters** (from `empath.inference`)
   - Accepts all Empath GenerationParams
   - Supports all task types (text2music, cover, repaint, etc.)
   - Uses existing LM and DiT models

3. **Project Storage**
   - Saves generated audio files
   - Tracks metadata with JSON
   - Compatible with existing workflows

## 📈 Next Steps (Future Roadmap)

**Phase 2 (v0.2.0):**
- [ ] Waveform visualization with interactive timeline
- [ ] Real-time progress visualization
- [ ] Preset save/load for generation settings
- [ ] Audio analysis (BPM detection, key detection)

**Phase 3 (v0.3.0):**
- [ ] Advanced mixing console (multi-track editing)
- [ ] Lyrics editor with music sync
- [ ] Export to different formats (MP3, FLAC)
- [ ] Cloud project sync

**Phase 4 (v0.4.0):**
- [ ] Electron wrapper for desktop app
- [ ] React upgrade for waveform editor
- [ ] Collaborative features
- [ ] Mobile app

## ⚡ Performance Tips

1. **First generation:** Takes longer (model loading)
2. **Use batch mode:** More efficient for multiple songs
3. **Enable Flash Attention:** Faster if GPU supports it
4. **Use turbo model:** Faster generation (lower quality)
5. **Enable CPU offload:** Reduce VRAM usage

## 🐛 Troubleshooting

### Models not found
```bash
# Let first generation auto-download or:
cd .. && python -m empath.model_downloader
```

### Port 8501 already in use
```bash
streamlit run main.py --server.port 8502
```

### Clear cache and start fresh
```bash
streamlit cache clear && streamlit run main.py
```

### CUDA out of memory
- Reduce inference steps in advanced settings
- Enable CPU offload in settings
- Use smaller model (turbo instead of base)

## 📚 Documentation

- **README.md** - Full user guide
- **INSTALL.md** - Detailed installation
- **config.py** - Configuration options
- **Main.py** - App routing and structure

## 🔗 Useful Links

- 🌍 [Empath Website](https://ace-step.github.io/)
- 🤗 [HuggingFace Model](https://huggingface.co/Empath/Empath1.5)
- 💬 [Discord Community](https://discord.gg/PeWDxrkdj7)
- 📄 [Technical Paper](https://arxiv.org/abs/2602.00744)
- 🐙 [GitHub Repository](https://github.com/ace-step/Empath-1.5)

## 🎯 Key Improvements Over Existing Gradio UI

| Feature | Gradio | ACE Studio |
|---------|--------|-----------|
| **Entry Point** | Technical config | Creative wizard |
| **Task Discovery** | Hidden dropdown | Prominent cards |
| **Visual Feedback** | Text logs | Progress bars |
| **Project Management** | Outputs folder | Dashboard with recents |
| **Editing** | Regenerate scratch | Non-linear by region |
| **Batch Support** | Separate UI | Integrated queue |
| **Settings** | Always visible | Hidden, toggle-able |
| **Mobile Support** | Poor | Responsive |

## 📝 Notes for Developers

- Config-driven design: Change `config.py` for UI customization
- Component-based: Easy to add new editing modes
- Session state management: Preserves state across reruns
- Handler caching: Efficient GPU memory usage
- Project persistence: JSON metadata + audio files

---

## 🎉 You're Ready!

Run the app and start generating music!

```bash
cd empath/ui/streamlit
./run.sh  # or run.bat on Windows
```

Questions? Check the docs or ask on Discord!

Happy music making! 🎵

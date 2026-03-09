
<h1 align="center">Empath 1.5</h1>
<h1 align="center">Pushing the Boundaries of Open-Source Music Generation</h1>
## 📝 Abstract
🚀 We present Empath , a highly efficient open-source music foundation model that brings commercial-grade generation to consumer hardware. On commonly used evaluation metrics, Empath   achieves quality beyond most commercial music models while remaining extremely fast—under 2 seconds per full song on an A100 and under 10 seconds on an RTX 3090. The model runs locally with less than 4GB of VRAM, and supports lightweight personalization: users can train a LoRA from just a few songs to capture their own style.

🌉 At its core lies a novel hybrid architecture where the Language Model (LM) functions as an omni-capable planner: it transforms simple user queries into comprehensive song blueprints—scaling from short loops to 10-minute compositions—while synthesizing metadata, lyrics, and captions via Chain-of-Thought to guide the Diffusion Transformer (DiT). ⚡ Uniquely, this alignment is achieved through intrinsic reinforcement learning relying solely on the model's internal mechanisms, thereby eliminating the biases inherent in external reward models or human preferences. 🎚️

🔮 Beyond standard synthesis, Empath   unifies precise stylistic control with versatile editing capabilities—such as cover generation, repainting, and vocal-to-BGM conversion—while maintaining strict adherence to prompts across 50+ languages. This paves the way for powerful tools that seamlessly integrate into the creative workflows of music artists, producers, and content creators. 🎸

## ✨ Features

### ⚡ Performance
- ✅ **Ultra-Fast Generation** — Under 2s per full song on A100, under 10s on RTX 3090 (0.5s to 10s on A100 depending on think mode & diffusion steps)
- ✅ **Flexible Duration** — Supports 10 seconds to 10 minutes (600s) audio generation
- ✅ **Batch Generation** — Generate up to 8 songs simultaneously

### 🎵 Generation Quality
- ✅ **Commercial-Grade Output** — Quality beyond most commercial music models (between Suno v4.5 and Suno v5)
- ✅ **Rich Style Support** — 1000+ instruments and styles with fine-grained timbre description
- ✅ **Multi-Language Lyrics** — Supports 50+ languages with lyrics prompt for structure & style control

### 🎛️ Versatility & Control

| Feature | Description |
|---------|-------------|
| ✅ Reference Audio Input | Use reference audio to guide generation style |
| ✅ Cover Generation | Create covers from existing audio |
| ✅ Repaint & Edit | Selective local audio editing and regeneration |
| ✅ Track Separation | Separate audio into individual stems |
| ✅ Multi-Track Generation | Add layers like Suno Studio's "Add Layer" feature |
| ✅ Vocal2BGM | Auto-generate accompaniment for vocal tracks |
| ✅ Metadata Control | Control duration, BPM, key/scale, time signature |
| ✅ Simple Mode | Generate full songs from simple descriptions |
| ✅ Query Rewriting | Auto LM expansion of tags and lyrics |
| ✅ Audio Understanding | Extract BPM, key/scale, time signature & caption from audio |
| ✅ LRC Generation | Auto-generate lyric timestamps for generated music |
| ✅ LoRA Training | One-click annotation & training in Gradio. 8 songs, 1 hour on 3090 (12GB VRAM) |
| ✅ Quality Scoring | Automatic quality assessment for generated audio |

## 🔔 Staying ahead
Star Empath on GitHub and be instantly notified of new releases

## 🤝 Partners
ComfyUI | Zilliz | Milvus | Zeabur

## ⚡ Quick Start

> **Requirements:** Python 3.11-3.12, CUDA GPU recommended (also supports MPS / ROCm / Intel XPU / CPU)
> 
> **Note:** ROCm on Windows requires Python 3.12 (AMD officially provides Python 3.12 wheels only)

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh          # macOS / Linux
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# 2. Clone & install
git clone https://github.com/dewanshshekhar/Swara.5.git
cd Empath-1.5
uv sync

# 3. Launch Gradio UI (models auto-download on first run)
uv run empath

# Or launch REST API server
uv run empath-api
```

Open http://localhost:7860 (Gradio) or http://localhost:8001 (API).

> 📦 **Windows users:** A portable package with pre-installed dependencies is available.

> 📖 **Full installation guide** (AMD/ROCm, Intel GPU, CPU, environment variables, command-line options) is available in the docs.

### 💡 Which Model Should I Choose?

## Recommended Language Model Based on GPU VRAM

| Your GPU VRAM | Recommended LM Model | Backend | Notes |
|---------------|----------------------|--------|------|
| ≤6GB | None (DiT only) | — | LM disabled by default; INT8 quantization + full CPU offload |
| 6–8GB | acestep-5Hz-lm-0.6B | pt | Lightweight LM with PyTorch backend |
| 8–16GB | acestep-5Hz-lm-0.6B / 1.7B | vllm | 0.6B for 8–12GB, 1.7B for 12–16GB |
| 16–24GB | acestep-5Hz-lm-1.7B | vllm | 4B available on 20GB+; no offload needed on 20GB+ |
| ≥24GB | acestep-5Hz-lm-4B | vllm | Best quality, all models fit without offload |

The UI automatically selects the best configuration for your GPU. All settings (LM model, backend, offloading, quantization) are tier-aware and pre-configured.

> 📖 GPU compatibility details are available in the docs.

## 🚀 Launch Scripts

Ready-to-use launch scripts for all platforms with auto environment detection, update checking, and dependency installation.

| Platform | Scripts | Backend |
|----------|---------|---------|
| **Windows** | `start_gradio_ui.bat`, `start_api_server.bat` | CUDA |
| **Windows (ROCm)** | `start_gradio_ui_rocm.bat`, `start_api_server_rocm.bat` | AMD ROCm |
| **Linux** | `start_gradio_ui.sh`, `start_api_server.sh` | CUDA |
| **macOS** | `start_gradio_ui_macos.sh`, `start_api_server_macos.sh` | MLX (Apple Silicon) |

```bash
# Windows
start_gradio_ui.bat

# Linux
chmod +x start_gradio_ui.sh && ./start_gradio_ui.sh

# macOS (Apple Silicon)
chmod +x start_gradio_ui_macos.sh && ./start_gradio_ui_macos.sh
```

### ⚙️ Customizing Launch Settings

**Recommended:** Create a `.env` file to customize models, ports, and other settings. Your `.env` configuration will survive repository updates.

```bash
# Copy the example file
cp .env.example .env

# Edit with your preferred settings
# Examples in .env:
EMPATH_CONFIG_PATH=empath-v15-turbo
EMPATH_LM_MODEL_PATH=empath-5Hz-lm-1.7B
PORT=7860
LANGUAGE=en
```

## 📚 Documentation

### Usage Guides

| Method | Description |
|--------|-------------|
| 🖥️ **Gradio Web UI** | Interactive web interface for music generation |
| 🎚️ **Studio UI** | Optional HTML frontend (DAW-like) |
| 🐍 **Python API** | Programmatic access for integration |
| 🌐 **REST API** | HTTP-based async API for services |
| ⌨️ **CLI** | Interactive wizard and configuration |

### Setup & Configuration

| Topic |
|-------|
| 📦 Installation (all platforms) |
| 🎮 GPU Compatibility |
| 🔧 GPU Troubleshooting |
| 🔬 Benchmark & Profiling |

### Multi-Language Docs
Available in English, Chinese, Japanese, and Korean in the `docs` folder.

## 📖 Tutorial

**🎯 Must Read:** Comprehensive guide to Empath 1.5's design philosophy and usage methods.

Available in English, Chinese, and Japanese in the `docs` folder.

This tutorial covers: mental models and design philosophy, model architecture and selection, input control (text and audio), inference hyperparameters, random factors and optimization strategies.

## 🔨 Train

📖 **LoRA Training Tutorial** — step-by-step guide covering data preparation, annotation, preprocessing, and training available in the `docs` folder.

See also the **LoRA Training** tab in Gradio UI for one-click training.

🔧 **Advanced Training with Side-Step** — CLI-based training toolkit with corrected timestep sampling, LoKR adapters, VRAM optimization, gradient sensitivity analysis, and more.

## 🏗️ Architecture
Empath Framework (refer to local docs/assets for architecture diagrams)

## 🦁 Model Zoo

### DiT Models

| DiT Model | Pre-Training | SFT | RL | CFG | Step | Refer audio | Text2Music | Cover | Repaint | Extract | Lego | Complete | Quality | Diversity | Fine-Tunability | 
|-----------|:------------:|:---:|:--:|:---:|:----:|:-----------:|:----------:|:-----:|:-------:|:-------:|:----:|:--------:|:-------:|:---------:|:---------------:|
| `empath-v15-base` | ✅ | ❌ | ❌ | ✅ | 50 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Medium | High | Easy | 
| `empath-v15-sft` | ✅ | ✅ | ❌ | ✅ | 50 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | High | Medium | Easy | 
| `empath-v15-turbo` | ✅ | ✅ | ❌ | ❌ | 8 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | Very High | Medium | Medium | 
| `empath-v15-turbo-rl` | ✅ | ✅ | ✅ | ❌ | 8 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | Very High | Medium | Medium | 

### LM Models

| LM Model | Pretrain from | Pre-Training | SFT | RL | CoT metas | Query rewrite | Audio Understanding | Composition Capability | Copy Melody | 
|----------|---------------|:------------:|:---:|:--:|:---------:|:-------------:|:-------------------:|:----------------------:|:-----------:|
| `empath-5Hz-lm-0.6B` | Qwen3-0.6B | ✅ | ✅ | ✅ | ✅ | ✅ | Medium | Medium | Weak | 
| `empath-5Hz-lm-1.7B` | Qwen3-1.7B | ✅ | ✅ | ✅ | ✅ | ✅ | Medium | Medium | Medium | 
| `empath-5Hz-lm-4B` | Qwen3-4B | ✅ | ✅ | ✅ | ✅ | ✅ | Strong | Strong | Strong | 

## 🔬 Benchmark

Empath 1.5 includes `profile_inference.py`, a profiling & benchmarking tool that measures LLM, DiT, and VAE timing across devices and configurations.

```bash
python profile_inference.py                        # Single-run profile
python profile_inference.py --mode benchmark       # Configuration matrix
```


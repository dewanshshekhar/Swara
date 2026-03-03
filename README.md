<h1 align="center">Swara</h1>
<h1 align="center">A Step Towards Music Generation Foundation Model</h1>
<p align="center">
    <a href="https://ace-step.github.io/">Project</a> |
    <a href="https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B">Hugging Face</a> |
    <a href="https://modelscope.cn/models/ACE-Step/ACE-Step-v1-3.5B">ModelScope</a> |
    <a href="https://discord.gg/PeWDxrkdj7">Discord</a>
</p>

## 📝 Introduction

Welcome to **Swara v1.0**! 

Swara is a novel open-source foundation model for music generation designed for high performance, musical coherence, and advanced controllability. It leverages diffusion-based generation to create high-quality music tracks quickly, acting as a flexible architecture for various music AI sub-tasks. Our mission is to build the *Stable Diffusion moment for music*, enabling creators, producers, and developers to easily integrate state-of-the-art music generation into their workflows.

## ✨ Key Features

- **Blazing Fast Generation**: Synthesize up to 4 minutes of music in just 20 seconds on an A100 GPU.
- **Diverse Styles & Genres**: Support for mainstream and niche music styles through descriptive text and tags.
- **Multilingual Support**: Generate vocals in up to 19 languages, optimized for English, Chinese, Japanese, and more.
- **Advanced Controllability**: Control parameters such as track stem variations, lyrics editing, and specific instrumental styling.
- **Voice & Instrument Rendering**: Highly detailed vocal performances and acoustic nuances for complex multi-instrumental arrangements.

## 📦 Installation

It is highly recommended to use a virtual environment like `conda`. Ensure you have Python 3.10+ installed.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dewanshshekhar/Swara.git
   cd Swara
   ```

2. **Create and Activate Environment**:
   ```bash
   conda create -n swara python=3.10 -y
   conda activate swara
   ```

3. **Install Dependencies**:
   For Windows users with NVIDIA GPUs, install PyTorch with CUDA support first:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
   ```

   Then install Swara:
   ```bash
   pip install -e .
   ```

## 🚀 Quick Start

To launch the local Gradio interface, simply run:

```bash
swara --port 7865
```

Navigate to `http://127.0.0.1:7865/` in your browser.

**Advanced UI Launch**:
```bash
swara --port 7865 --device_id 0 --share true --bf16 true
```
*Note: Use `--bf16 false` if you are on macOS.*

### Memory Optimization for Consumer GPUs (8GB VRAM)
If you have limited VRAM (e.g., 8GB), use the following flags to offload weights and optimize decoding natively:
```bash
swara --torch_compile true --cpu_offload true --overlapped_decode true
```

## 📂 Models & Checkpoints

The system will automatically download the default required model checkpoints on its first run to `~/.cache/swara/checkpoints`. To specify a custom model directory, use the `--checkpoint_path` argument.

## 🤝 Community & Support

- **Discord**: Join our community to share your generations and ask questions!
- **Contributions**: We welcome PRs! Whether it's to add more SSML tags or new musical features, please feel free to contribute to the Swara foundation.

## 📜 Disclaimer

Swara is a tool for creative production and entertainment. Users are responsible for ensuring the originality of generated works, clearly disclosing AI involvement, and securing permissions for any adapted styles or materials. The authors are not responsible for the creation of inappropriate or harmful content.

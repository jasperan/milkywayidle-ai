# Getting Started

This guide will help you set up and start using the Milky Way Idle AI Assistant.

## System Requirements

- Windows 10/11, macOS, or Linux
- Python 3.8 or higher
- Ollama installed and running
- At least 8GB RAM (16GB recommended)
- GPU with CUDA support (optional, but recommended)

## Installation Steps

### 1. Install Ollama

First, install Ollama on your system:

- **Windows**: Download and run the installer from [Ollama's website](https://ollama.ai/)
- **macOS**: 
  ```bash
  brew install ollama
  ```
- **Linux**:
  ```bash
  curl -fsSL https://ollama.ai/install.sh | sh
  ```

### 2. Pull the LLaVA Model

Open a terminal and run:
```bash
ollama pull llava
```

This may take some time depending on your internet connection.

### 3. Set Up Python Environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Assistant

1. Start Ollama (if not already running):
   ```bash
   ollama serve
   ```

2. In a new terminal, run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## First-Time Setup

1. In the sidebar:
   - Verify that the LLaVA model is available
   - Enable automatic screenshot capture if desired
   - Adjust any other settings as needed

2. In the main interface:
   - Upload a screenshot of your game
   - Ask your first question about progression
   - The AI will analyze your game state and provide suggestions

## Troubleshooting

If you encounter any issues:

1. Check that Ollama is running:
   ```bash
   ollama list
   ```

2. Verify the LLaVA model is available:
   ```bash
   ollama pull llava
   ```

3. Check your Python environment:
   ```bash
   pip list
   ```

4. Review the error messages in the Streamlit interface

For more detailed troubleshooting, see the [FAQ](faq.md) and [Technical Documentation](technical.md).

## Next Steps

- Learn about [Features](features.md)
- Read the [User Guide](user-guide.md)
- Explore [Advanced Usage](technical.md#advanced-usage)

## Support

If you need help:
- Check the [FAQ](faq.md)
- Open an issue on GitHub
- Join our Discord community 
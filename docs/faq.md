# Frequently Asked Questions

## General Questions

### What is the Milky Way Idle AI Assistant?
The Milky Way Idle AI Assistant is a tool that helps you progress in the Milky Way Idle game by analyzing screenshots and providing strategic advice using the LLaVA vision-language model.

### How does it work?
The assistant captures screenshots of your game, analyzes them using LLaVA, and provides specific advice on how to progress. It can work in both manual and automatic modes.

### Is it safe to use?
Yes, the assistant:
- Runs locally on your machine
- Doesn't modify game files
- Doesn't share your data
- Only analyzes screenshots

## Installation

### What are the system requirements?
- Python 3.8 or higher
- 8GB RAM minimum (16GB recommended)
- NVIDIA GPU with 4GB VRAM (recommended)
- 1GB free storage space

### How do I install Ollama?
1. Visit [Ollama's website](https://ollama.ai/)
2. Download the installer for your OS
3. Run the installer
4. Start the Ollama service

### How do I pull the LLaVA model?
```bash
ollama pull llava
```

## Usage

### How do I start the assistant?
1. Install dependencies: `pip install -r requirements.txt`
2. Start Streamlit: `streamlit run app.py`
3. Open your browser to `http://localhost:8501`

### How do I capture screenshots?
You have three options:
1. Manual capture: Click "Capture Current Screen"
2. Automatic capture: Enable in sidebar settings
3. Upload: Use the file uploader

### How often does it capture screenshots?
By default, every 30 seconds when auto-capture is enabled. This can be adjusted in the settings.

## Model Management

### Which LLaVA model should I use?
- `llava:latest` (recommended)
- `llava:13b` (more accurate, slower)
- `llava:7b` (faster, less accurate)

### How do I check if the model is available?
Click "Check Model Status" in the sidebar. You'll see:
- ✅ Model is available
- ⚠️ Model not found
- ❌ Error checking status

### How do I pull a new model?
1. Select the model in the sidebar
2. Click "Pull Model"
3. Wait for the download to complete

## Troubleshooting

### The model isn't working
1. Check if Ollama is running: `ollama list`
2. Verify the model is pulled: `ollama list`
3. Check the Streamlit logs for errors
4. Try pulling the model again

### Screenshot capture isn't working
1. Ensure the game is visible on your primary monitor
2. Check if you have screen capture permissions
3. Verify mss is installed: `pip install mss`
4. Try manual capture first

### The assistant is slow
1. Use a smaller model (llava:7b)
2. Reduce screenshot quality
3. Increase capture interval
4. Check your system resources

### Progress tracking isn't updating
1. Check if auto-capture is enabled
2. Verify storage permissions
3. Check the data directory
4. Try clearing and restarting

## Advanced Usage

### Can I customize the capture interval?
Yes, you can modify the `SCREENSHOT_INTERVAL` in the settings or environment variables.

### How do I change the model settings?
1. In the sidebar, select a different model
2. Click "Check Model Status"
3. Pull the new model if needed

### Can I export my progress data?
Yes, the progress data is stored in JSON format in the data directory.

## Privacy and Security

### Where is my data stored?
All data is stored locally in the `data` directory:
- Screenshots
- Progress data
- Configuration

### Is my data shared?
No, all processing happens locally and no data is shared externally.

### How do I clear my data?
1. Stop the assistant
2. Delete the `data` directory
3. Restart the assistant

## Performance

### Why is it using so much CPU/GPU?
The LLaVA model requires significant resources for:
- Image processing
- Model inference
- Analysis generation

### How can I reduce resource usage?
1. Use a smaller model
2. Increase capture interval
3. Reduce screenshot quality
4. Close other resource-intensive applications

### What's the optimal setup?
- 16GB RAM
- NVIDIA GPU with 8GB VRAM
- Fast SSD storage
- Recent CPU (4+ cores)

## Development

### Can I contribute to the project?
Yes! The project is open source. Check the [Development](development.md) guide for details.

### How do I report bugs?
1. Check if the issue is already reported
2. Create a new issue on GitHub
3. Include:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - System information

### Where can I get help?
1. Check this FAQ
2. Review the documentation
3. Open a GitHub issue
4. Join the Discord community 
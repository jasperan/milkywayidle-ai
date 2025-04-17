# Technical Details

This document provides technical information about the Milky Way Idle AI Assistant's architecture, requirements, and implementation details.

## System Architecture

### Components
1. Frontend (Streamlit)
   - User Interface
   - Screenshot Capture
   - Chat Interface
   - Progress Display

2. Backend (Python)
   - Ollama Integration
   - Image Processing
   - Data Management
   - Analysis Engine

3. Storage
   - Progress Data (JSON)
   - Screenshot Cache
   - Configuration Files

### Data Flow
1. User Interaction
   ```
   User -> Streamlit UI -> Python Backend -> Ollama -> Response
   ```

2. Screenshot Processing
   ```
   Screen Capture -> Image Processing -> Model Analysis -> Progress Tracking
   ```

3. Progress Tracking
   ```
   Analysis Results -> JSON Storage -> Progress Display -> User Feedback
   ```

### Supported Models

#### LLaVA Models
- `llava:latest`: Latest version of LLaVA
- `llava:13b`: 13B parameter model
- `llava:7b`: 7B parameter model

#### Gemma 3 Models
- `gemma3:4b`: 4B parameter model with 128K context window
- `gemma3:12b`: 12B parameter model with 128K context window
- `gemma3:27b`: 27B parameter model with 128K context window

All models support:
- Multimodal processing (text and images)
- 128K context window
- Over 140 languages
- Question answering
- Summarization
- Reasoning tasks

## System Requirements

### Hardware
- CPU: Dual-core 2.0 GHz or better
- RAM: 8GB minimum (16GB recommended)
- GPU: NVIDIA GPU with 4GB VRAM (recommended)
- Storage: 1GB free space

### Software
- Python 3.8 or higher
- Ollama runtime (for local mode)
- Streamlit
- Required Python packages (see requirements.txt)

### Operating Systems
- Windows 10/11
- macOS 10.15 or later
- Linux (Ubuntu 20.04 or later)

## Dependencies

### Core Dependencies
```python
streamlit>=1.32.0      # Web interface
ollama>=0.1.6         # Model integration
Pillow>=10.2.0        # Image processing
mss>=9.0.1           # Screenshot capture
requests>=2.31.0     # HTTP client
```

### Optional Dependencies
```python
numpy>=1.21.0        # Numerical operations
opencv-python>=4.5.0 # Advanced image processing
pandas>=1.3.0        # Data analysis
```

## Configuration

### Environment Variables
```bash
OLLAMA_HOST=localhost    # Ollama server host
OLLAMA_PORT=11434       # Ollama server port
SCREENSHOT_INTERVAL=30  # Capture interval in seconds
```

### App Configuration
```python
# Default settings
DEFAULT_MODEL = "llava:latest"
SCREENSHOT_QUALITY = 85
MAX_HISTORY = 100
STORAGE_PATH = "./data"

# Model configurations
MODEL_CONFIGS = {
    "llava:latest": {
        "name": "LLaVA Latest",
        "description": "Latest version of LLaVA model",
        "supports_images": True
    },
    "llava:13b": {
        "name": "LLaVA 13B",
        "description": "13B parameter LLaVA model",
        "supports_images": True
    },
    "llava:7b": {
        "name": "LLaVA 7B",
        "description": "7B parameter LLaVA model",
        "supports_images": True
    },
    "gemma3:4b": {
        "name": "Gemma 3 4B",
        "description": "4B parameter Gemma 3 model with 128K context window",
        "supports_images": True
    },
    "gemma3:12b": {
        "name": "Gemma 3 12B",
        "description": "12B parameter Gemma 3 model with 128K context window",
        "supports_images": True
    },
    "gemma3:27b": {
        "name": "Gemma 3 27B",
        "description": "27B parameter Gemma 3 model with 128K context window",
        "supports_images": True
    }
}
```

### Distributed Mode Configuration
```python
# Distributed mode settings
USE_DISTRIBUTED = False  # Enable distributed mode
DISTRIBUTED_HOST = "http://localhost:11434"  # Remote Ollama host
```

## Implementation Details

### Screenshot Capture
```python
def capture_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        return Image.frombytes('RGB', screenshot.size, screenshot.rgb)
```

### Model Integration
```python
def analyze_screenshot(image_bytes):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Analyze this screenshot...", "images": [image_bytes]}
    ]
    response = ollama.chat(model=MODEL_NAME, messages=messages)
    return response['message']['content']
```

### Distributed Mode Client
```python
def get_distributed_response(messages, model_name):
    try:
        # Convert image to base64 if present
        if "images" in messages[1]:
            image_bytes = messages[1]["images"][0]
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            messages[1]["images"] = [image_base64]
        
        response = requests.post(
            f"{DISTRIBUTED_HOST}/api/chat",
            json={
                "model": model_name,
                "messages": messages
            }
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except Exception as e:
        st.error(f"Error in distributed mode: {str(e)}")
        return None
```

### Progress Tracking
```python
def update_progress(analysis):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    progress_data = {
        "timestamp": timestamp,
        "analysis": analysis,
        "suggestions": extract_suggestions(analysis),
        "achievements": track_achievements(analysis)
    }
    save_progress(progress_data)
```

## Performance Considerations

### Model Performance
1. LLaVA Models
   - Fast inference times
   - Good image understanding
   - Moderate resource usage

2. Gemma 3 Models
   - 4B: Lightweight, fast inference
   - 12B: Balanced performance
   - 27B: High accuracy, more resources

### Optimization Techniques
1. Image Processing
   - Compression
   - Resolution scaling
   - Format conversion

2. Model Inference
   - Batch processing
   - Caching
   - Parallel processing

3. Storage Management
   - Data compression
   - Cleanup routines
   - Cache limits

### Resource Usage
- CPU: 10-30% during analysis
- RAM: 2-4GB typical usage
- GPU: 2-4GB VRAM for models
- Storage: ~100MB per day

### Distributed Mode Performance
- Network latency considerations
- Image transfer optimization
- Connection pooling
- Error handling and retries

## Security

### Data Protection
- Local storage only
- No external API calls (in local mode)
- Encrypted configuration
- Secure file handling

### Privacy
- Screenshots stored locally
- No data sharing (in local mode)
- User-controlled retention
- Secure deletion

### Distributed Mode Security
- HTTPS support
- API key authentication
- Rate limiting
- Input validation

## Error Handling

### Common Errors
1. Model Errors
   - Connection issues
   - Model not found
   - Inference failures

2. Capture Errors
   - Permission denied
   - Monitor not found
   - Format issues

3. Storage Errors
   - Disk full
   - Permission denied
   - File corruption

4. Distributed Mode Errors
   - Network connectivity
   - API endpoint issues
   - Authentication failures
   - Rate limiting

### Recovery Procedures
1. Automatic
   - Retry mechanisms
   - Fallback options
   - Error logging

2. Manual
   - Reset procedures
   - Data recovery
   - Configuration reset

## Monitoring

### Logging
- Error logs
- Performance metrics
- User actions
- System events

### Metrics
- Capture success rate
- Analysis time
- Model performance
- Storage usage
- Network latency (distributed mode)

## Development

### Code Structure
```
milkywayidle-ai/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── docs/              # Documentation
├── data/              # Storage
└── tests/             # Test suite
```

### Testing
- Unit tests
- Integration tests
- Performance tests
- User acceptance tests
- Distributed mode tests

## Deployment

### Local Deployment
1. Install dependencies
2. Configure environment
3. Start Ollama
4. Run Streamlit app

### Distributed Mode Deployment
1. Set up remote Ollama instance
2. Configure network access
3. Update distributed mode settings
4. Test connectivity

### Production Considerations
- Resource monitoring
- Error tracking
- Backup procedures
- Update management 
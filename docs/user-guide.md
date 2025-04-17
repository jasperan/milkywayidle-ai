# User Guide

This guide provides detailed instructions on how to use the Milky Way Idle AI Assistant effectively.

## Interface Overview

The assistant's interface is divided into two main sections:

### 1. Sidebar
- Model Settings
- Auto-Capture Settings
- Progress Tracking

### 2. Main Interface
- Chat Display
- Screenshot Controls
- Input Area

## Model Management

### Available Models

#### LLaVA Models
- `llava:latest`: Latest version of LLaVA (recommended for most users)
- `llava:13b`: 13B parameter model (more accurate, slower)
- `llava:7b`: 7B parameter model (faster, less accurate)

#### Gemma 3 Models
- `gemma3:4b`: 4B parameter model (lightweight, fast)
- `gemma3:12b`: 12B parameter model (balanced performance)
- `gemma3:27b`: 27B parameter model (high accuracy, more resources)

All models support:
- Image analysis
- Text processing
- Multilingual support
- Long context windows

### Selecting a Model
1. In the sidebar, find the "Model Settings" section
2. Use the dropdown to select your preferred model
3. Consider your system resources and needs:
   - For low-resource systems: `llava:7b` or `gemma3:4b`
   - For balanced performance: `llava:latest` or `gemma3:12b`
   - For maximum accuracy: `llava:13b` or `gemma3:27b`

### Checking Model Status
1. Click the "Check Model Status" button
2. The system will verify if the selected model is available
3. You'll see one of these messages:
   - ✅ Model is available
   - ⚠️ Model not found
   - ❌ Error checking status

### Pulling a Model
If the model is not available:
1. Click the "Pull Model" button
2. Wait for the download to complete
3. Monitor the progress in the status area
4. The model will be ready when the download finishes

## Screenshot Capture

### Manual Capture
1. Click the "Capture Current Screen" button
2. The system will capture your primary monitor
3. The screenshot will appear in the chat interface
4. You can now ask questions about the captured image

### Automatic Capture
1. In the sidebar, find "Auto-Capture Settings"
2. Toggle the "Enable Automatic Screenshot Capture" switch
3. The system will:
   - Capture screenshots every 30 seconds
   - Analyze the game state
   - Provide proactive suggestions
   - Track progress over time

### Uploading Screenshots
1. Click the "Upload a screenshot" button
2. Select an image file (PNG, JPG, JPEG)
3. The image will appear in the chat interface
4. You can now ask questions about the uploaded image

## Chat Usage

### Basic Chat
1. Type your question in the chat input
2. Press Enter or click Send
3. The AI will respond with advice and suggestions
4. Continue the conversation as needed

### Image-Based Questions
1. Capture or upload a screenshot
2. Type your question about the image
3. The AI will analyze the image and respond
4. You can ask follow-up questions

### Effective Questioning
For best results, try questions like:
- "What should I focus on next?"
- "How can I optimize my resources?"
- "What achievements should I prioritize?"
- "What upgrades should I get next?"

## Progress Tracking

### Viewing Progress
1. In the sidebar, find "Progress Tracking"
2. View the last analysis timestamp and content
3. Check current suggestions and achievements
4. Monitor resource optimization tips

### Understanding Analysis
The system provides:
1. Current Game State
   - Resource levels
   - Achievement progress
   - Available upgrades
   - Current objectives

2. Next Steps
   - Immediate actions
   - Short-term goals
   - Resource management
   - Achievement focus

3. Long-term Strategy
   - Progression path
   - Resource optimization
   - Achievement planning
   - Upgrade priorities

## Best Practices

### For Best Results
1. Keep the game visible on your primary monitor
2. Enable auto-capture for continuous analysis
3. Ask specific questions about your current situation
4. Review progress tracking regularly

### Common Use Cases
1. Early Game
   - Focus on basic resource management
   - Prioritize initial upgrades
   - Follow achievement paths

2. Mid Game
   - Optimize resource production
   - Plan upgrade sequences
   - Track achievement progress

3. Late Game
   - Maximize efficiency
   - Complete remaining achievements
   - Optimize endgame strategies

## Troubleshooting

### Common Issues
1. Model Not Available
   - Check Ollama is running
   - Verify model name
   - Try pulling the model again

2. Screenshot Issues
   - Ensure game is visible
   - Check monitor settings
   - Verify capture permissions

3. Analysis Problems
   - Check image quality
   - Verify game visibility
   - Ensure proper lighting

### Getting Help
1. Check the [FAQ](faq.md)
2. Review error messages
3. Check system requirements
4. Contact support if needed

## Advanced Usage

### Custom Configuration
1. Environment Variables
   - Set custom Ollama host
   - Configure ports
   - Adjust timeouts

2. App Settings
   - Modify capture interval
   - Adjust quality settings
   - Configure storage options

### Data Management
1. Progress Data
   - View history
   - Export data
   - Clear history

2. Screenshot Storage
   - Manage storage
   - Configure retention
   - Set quality preferences 
import streamlit as st
import ollama
import time
from PIL import Image
import io
import mss
import mss.tools
import threading
import json
import os
from datetime import datetime
import requests
import base64

# Set page config
st.set_page_config(
    page_title="Milky Way Idle AI Assistant",
    page_icon="🌌",
    layout="wide"
)

# Constants
SCREENSHOT_INTERVAL = 30  # seconds
SYSTEM_PROMPT = """You are a Milky Way Idle game assistant. Your task is to analyze screenshots of the game and provide specific advice on how to progress. 
Focus on:
1. Current game state analysis
2. Immediate next steps
3. Long-term strategy suggestions
4. Resource optimization
5. Achievement progress

Be concise and action-oriented in your responses."""

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

# Initialize session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model_ready" not in st.session_state:
    st.session_state.model_ready = False

if "last_screenshot" not in st.session_state:
    st.session_state.last_screenshot = None

if "progress_data" not in st.session_state:
    st.session_state.progress_data = {
        "last_analysis": None,
        "suggestions": [],
        "achievements": {},
        "resources": {}
    }

if "auto_capture" not in st.session_state:
    st.session_state.auto_capture = False

if "use_distributed" not in st.session_state:
    st.session_state.use_distributed = False

if "distributed_host" not in st.session_state:
    st.session_state.distributed_host = "http://localhost:11434"

# Distributed mode client
def get_distributed_response(messages, model_name):
    try:
        # Convert image to base64 if present
        if "images" in messages[1]:
            image_bytes = messages[1]["images"][0]
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            messages[1]["images"] = [image_base64]
        
        response = requests.post(
            f"{st.session_state.distributed_host}/api/chat",
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

# Screenshot capture function
def capture_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Primary monitor
        screenshot = sct.grab(monitor)
        return Image.frombytes('RGB', screenshot.size, screenshot.rgb)

# Periodic analysis function
def periodic_analysis():
    while st.session_state.auto_capture:
        try:
            # Capture screenshot
            screenshot = capture_screenshot()
            screenshot_bytes = io.BytesIO()
            screenshot.save(screenshot_bytes, format='PNG')
            screenshot_bytes = screenshot_bytes.getvalue()
            
            # Prepare message for LLaVA
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": "Analyze this screenshot and tell me what to do next to progress in the game.", "images": [screenshot_bytes]}
            ]
            
            # Get response based on mode
            if st.session_state.use_distributed:
                analysis = get_distributed_response(messages, st.session_state.current_model)
            else:
                response = ollama.chat(model=st.session_state.current_model, messages=messages)
                analysis = response['message']['content']
            
            if analysis:
                # Update progress data
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.progress_data["last_analysis"] = {
                    "timestamp": timestamp,
                    "analysis": analysis
                }
                
                # Add to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"🔄 Periodic Analysis ({timestamp}):\n{analysis}",
                    "image": screenshot
                })
            
            # Wait for next interval
            time.sleep(SCREENSHOT_INTERVAL)
            
        except Exception as e:
            st.error(f"Error in periodic analysis: {str(e)}")
            time.sleep(5)  # Wait before retrying

# Title and description
st.title("🌌 Milky Way Idle AI Assistant")
st.markdown("""
This assistant uses LLaVA to help you progress in Milky Way Idle. 
Upload screenshots or enable automatic capture to get continuous advice!
""")

# Sidebar for model management and settings
with st.sidebar:
    st.header("Model Settings")
    
    # Distributed mode toggle
    use_distributed = st.checkbox("Use Distributed Mode", value=st.session_state.use_distributed)
    if use_distributed != st.session_state.use_distributed:
        st.session_state.use_distributed = use_distributed
    
    if st.session_state.use_distributed:
        distributed_host = st.text_input("Distributed Host", value=st.session_state.distributed_host)
        if distributed_host != st.session_state.distributed_host:
            st.session_state.distributed_host = distributed_host
    
    # Model selection with descriptions
    model_name = st.selectbox(
        "Select Model",
        list(MODEL_CONFIGS.keys()),
        format_func=lambda x: f"{MODEL_CONFIGS[x]['name']} - {MODEL_CONFIGS[x]['description']}",
        index=0
    )
    st.session_state.current_model = model_name
    
    # Model status
    if st.button("Check Model Status"):
        try:
            if st.session_state.use_distributed:
                response = requests.get(f"{st.session_state.distributed_host}/api/tags")
                response.raise_for_status()
                available_models = [model["name"] for model in response.json()["models"]]
            else:
                models = ollama.list().models
                available_models = [model.model for model in models]
            
            if model_name in available_models:
                st.success(f"✅ {MODEL_CONFIGS[model_name]['name']} is available!")
                st.session_state.model_ready = True
            else:
                st.warning(f"⚠️ {MODEL_CONFIGS[model_name]['name']} not found. Please pull it first.")
                st.session_state.model_ready = False
        except Exception as e:
            st.error(f"❌ Error checking model status: {str(e)}")
            st.session_state.model_ready = False
    
    # Pull model button
    if st.button("Pull Model"):
        try:
            with st.spinner(f"Pulling {MODEL_CONFIGS[model_name]['name']}..."):
                if st.session_state.use_distributed:
                    response = requests.post(
                        f"{st.session_state.distributed_host}/api/pull",
                        json={"name": model_name}
                    )
                    response.raise_for_status()
                    st.success(f"✅ Successfully pulled {MODEL_CONFIGS[model_name]['name']}!")
                else:
                    progress_text = ""
                    for progress in ollama.pull(model_name, stream=True):
                        status = progress.get('status')
                        if status:
                            progress_text = f"Status: {status}"
                            st.write(progress_text)
                        
                        if 'completed' in progress and 'total' in progress:
                            completed = progress['completed']
                            total = progress['total']
                            if total > 0:
                                percent = (completed / total) * 100
                                progress_text = f"Downloading: {percent:.1f}% ({completed}/{total})"
                                st.write(progress_text)
                    
                    st.success(f"✅ Successfully pulled {MODEL_CONFIGS[model_name]['name']}!")
                st.session_state.model_ready = True
        except Exception as e:
            st.error(f"❌ Error pulling model: {str(e)}")
            st.session_state.model_ready = False
    
    # Auto-capture settings
    st.header("Auto-Capture Settings")
    auto_capture = st.checkbox("Enable Automatic Screenshot Capture", value=st.session_state.auto_capture)
    if auto_capture != st.session_state.auto_capture:
        st.session_state.auto_capture = auto_capture
        if auto_capture and st.session_state.model_ready:
            # Start periodic analysis in a separate thread
            analysis_thread = threading.Thread(target=periodic_analysis)
            analysis_thread.daemon = True
            analysis_thread.start()
    
    # Progress tracking
    st.header("Progress Tracking")
    if st.session_state.progress_data["last_analysis"]:
        st.subheader("Last Analysis")
        st.write(f"Time: {st.session_state.progress_data['last_analysis']['timestamp']}")
        st.write(st.session_state.progress_data['last_analysis']['analysis'])

# Main chat interface
st.header("Chat with LLaVA")

# Image upload and manual capture
col1, col2 = st.columns(2)
with col1:
    uploaded_image = st.file_uploader("Upload a screenshot", type=["png", "jpg", "jpeg"])
with col2:
    if st.button("Capture Current Screen"):
        try:
            screenshot = capture_screenshot()
            st.session_state.last_screenshot = screenshot
            st.image(screenshot, caption="Captured Screenshot", use_column_width=True)
        except Exception as e:
            st.error(f"Error capturing screenshot: {str(e)}")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "image" in message:
            st.image(message["image"], caption="Game Screenshot", use_column_width=True)
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know about Milky Way Idle?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    current_image = uploaded_image if uploaded_image else st.session_state.last_screenshot
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
        if current_image:
            st.image(current_image, caption="Game Screenshot", use_column_width=True)
    
    # Generate response
    if st.session_state.model_ready:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Prepare the message for LLaVA
                    messages = [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt}
                    ]
                    
                    if current_image:
                        if isinstance(current_image, Image.Image):
                            image_bytes = io.BytesIO()
                            current_image.save(image_bytes, format='PNG')
                            image_bytes = image_bytes.getvalue()
                        else:
                            image_bytes = current_image.getvalue()
                        messages[1]["images"] = [image_bytes]
                    
                    # Get response based on mode
                    if st.session_state.use_distributed:
                        assistant_response = get_distributed_response(messages, model_name)
                    else:
                        response = ollama.chat(model=model_name, messages=messages)
                        assistant_response = response['message']['content']
                    
                    if assistant_response:
                        # Display and store response
                        st.markdown(assistant_response)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": assistant_response,
                            "image": current_image
                        })
                except Exception as e:
                    st.error(f"❌ Error getting response: {str(e)}")
    else:
        st.warning("⚠️ Please check and pull the model first in the sidebar.")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()

# Save progress data
def save_progress():
    with open("progress_data.json", "w") as f:
        json.dump(st.session_state.progress_data, f)

# Load progress data
def load_progress():
    if os.path.exists("progress_data.json"):
        with open("progress_data.json", "r") as f:
            st.session_state.progress_data = json.load(f)

# Initialize progress data
load_progress()

# Save progress periodically
if st.session_state.auto_capture:
    save_progress() 
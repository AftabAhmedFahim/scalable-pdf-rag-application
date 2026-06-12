import sys
from pathlib import Path
import streamlit as st

# Ensure import paths resolve cleanly
sys.path.append(str(Path(__file__).parent.resolve()))

from styles import apply_custom_styles
from components.sidebar import render_sidebar
from components.chat import render_chat_canvas

# Page configuration
st.set_page_config(
    page_title="DocuMind AI - Intelligent PDF RAG",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom Theme & Styling
apply_custom_styles()

# Render sidebar controls and retrieve top-k configuration
top_k = render_sidebar()

# Render chat interaction area
render_chat_canvas(top_k)

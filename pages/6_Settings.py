import streamlit as st
import os

from dotenv import load_dotenv

from config import MODEL_NAME
from agents.image_analyzer import test_connection


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📷",
    layout="wide"
)


load_dotenv()


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("⚙️ Settings")

st.write(
    "View the current configuration and manage "
    "your Instagram AI Assistant session."
)


st.divider()


# --------------------------------------------------
# AI CONFIGURATION
# --------------------------------------------------

st.header("🤖 AI Configuration")

api_key = os.getenv("GEMINI_API_KEY")


config_col1, config_col2 = st.columns(2)

with config_col1:

    st.subheader("Model")

    st.code(
        MODEL_NAME,
        language="text"
    )


with config_col2:

    st.subheader("Gemini API")

    if api_key:

        st.success(
            "✓ API key detected"
        )

    else:

        st.error(
            "✗ GEMINI_API_KEY not found"
        )


# --------------------------------------------------
# GEMINI CONNECTION TEST
# --------------------------------------------------

st.subheader("🔌 Gemini Connection Test")

st.write(
    "Test whether the currently configured Gemini model "
    "is responding correctly."
)


if st.button(
    "Test Gemini Connection",
    type="primary"
):

    with st.spinner(
        "Testing Gemini connection..."
    ):

        result = test_connection()


    if (
        isinstance(result, str)
        and result.startswith("❌")
    ):

        st.error(result)

    else:

        st.success(result)


st.divider()


# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

st.header("📂 Project Information")

st.info(
    """
**Instagram AI Assistant**

A multi-tool AI assistant designed to help photographers
analyze photographs, plan Instagram carousels, generate
Lightroom Classic editing recommendations, create captions,
and discover music that matches an image's mood.
"""
)


# --------------------------------------------------
# AVAILABLE FEATURES
# --------------------------------------------------

st.header("✨ Available Features")

features = [
    {
        "icon": "📷",
        "name": "Image Analysis",
        "description": (
            "Analyze photographs and receive AI-powered "
            "photography feedback."
        )
    },
    {
        "icon": "🎠",
        "name": "Carousel Planner",
        "description": (
            "Analyze multiple images and help plan "
            "an Instagram carousel."
        )
    },
    {
        "icon": "🎨",
        "name": "Lightroom Editor",
        "description": (
            "Generate fixed Adobe Lightroom Classic "
            "editing recommendations."
        )
    },
    {
        "icon": "📝",
        "name": "Caption Generator",
        "description": (
            "Generate multiple Instagram caption styles "
            "based on an uploaded photograph."
        )
    },
    {
        "icon": "🎵",
        "name": "Music Suggestions",
        "description": (
            "Recommend music based on the mood and "
            "visual aesthetic of a photograph."
        )
    }
]


for feature in features:

    with st.container(border=True):

        st.markdown(
            f"### {feature['icon']} {feature['name']}"
        )

        st.write(
            feature["description"]
        )


st.divider()


# --------------------------------------------------
# SESSION MANAGEMENT
# --------------------------------------------------

st.header("🧹 Session Management")

st.write(
    "Clear generated results currently stored "
    "in this Streamlit session."
)


if st.button(
    "Clear Session Results",
    type="secondary"
):

    keys_to_remove = [

        # Image Analysis
        "image_analysis_result",
        "image_analysis_filename",

        # Lightroom Editor
        "lightroom_result",
        "lightroom_filename",

        # Caption Generator
        "caption_result",
        "caption_filename",

        # Music Suggestions
        "music_result",
        "music_filename"
    ]


    for key in keys_to_remove:

        if key in st.session_state:

            del st.session_state[key]


    st.success(
        "Session results cleared successfully."
    )


st.divider()


# --------------------------------------------------
# SECURITY NOTE
# --------------------------------------------------

st.caption(
    "Your Gemini API key is loaded from your local "
    ".env file and is not displayed by this application."
)
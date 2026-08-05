import streamlit as st

st.set_page_config(
    page_title="Dayyan's Instagram AI Assistant",
    page_icon="📷",
    layout="wide"
)

st.title("📷 Dayyan's Instagram AI Assistant")

st.markdown("""
## Welcome!

This AI assistant is built specifically for professional Instagram photography.

Use the sidebar to navigate between tools.

### Available Features

- 📷 Image Analysis
- 🎠 Carousel Planner
- 🎨 Lightroom Editor
- ✍️ Caption Generator
- 🎵 Music Suggestions

---

Made using Python + Streamlit + Google Gemini
""")
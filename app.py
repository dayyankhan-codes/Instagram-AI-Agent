from agents.image_analyzer import (
    test_connection,
    analyze_image
)
import streamlit as st

st.set_page_config(
    page_title="Dayyan's Instagram AI Assistant",
    page_icon="📷",
    layout="wide"
)

st.title("📷 Dayyan's Instagram AI Assistant")

st.write("Welcome! This app will help analyze your photos for Instagram.")

if st.button("Test Gemini Connection"):
    with st.spinner("Connecting to Gemini..."):
        result = test_connection()

    st.success(result)

uploaded_files = st.file_uploader(
    "Upload your photos",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:

    first_image = uploaded_files[0]

    if st.button("Analyze First Image"):

        with st.spinner("Gemini is analyzing your photo..."):

            result = analyze_image(first_image)

        st.markdown(result)

if uploaded_files:
    st.success(f"You uploaded {len(uploaded_files)} photo(s).")

    for file in uploaded_files:
        st.image(file, caption=file.name, use_container_width=True)
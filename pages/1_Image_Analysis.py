import streamlit as st

from agents.image_analyzer import (
    test_connection,
    analyze_image
)

st.title("📷 Image Analysis")

if st.button("Test Gemini Connection"):

    with st.spinner("Connecting to Gemini..."):

        result = test_connection()

    st.success(result)

uploaded_files = st.file_uploader(
    "Upload Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"{len(uploaded_files)} image(s) uploaded.")

    for file in uploaded_files:
        st.image(file, use_container_width=True)

    if st.button("Analyze First Image"):

        with st.spinner("Analyzing image..."):

            result = analyze_image(uploaded_files[0])

        st.markdown(result)
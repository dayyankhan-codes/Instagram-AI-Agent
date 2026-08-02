import streamlit as st

from agents.image_analyzer import analyze_image

st.set_page_config(
    page_title="Dayyan's Instagram AI Assistant",
    page_icon="📷",
    layout="wide"
)

st.title("📷 Dayyan's Instagram AI Assistant")

st.write("Upload one or more photos to analyze them with AI.")

uploaded_files = st.file_uploader(
    "Upload your photos",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"You uploaded {len(uploaded_files)} photo(s).")

    for file in uploaded_files:
        st.image(file, caption=file.name, use_container_width=True)

    if st.button("Analyze First Image"):

        with st.spinner("Analyzing image..."):

            result = analyze_image(uploaded_files[0])

        st.markdown(result)
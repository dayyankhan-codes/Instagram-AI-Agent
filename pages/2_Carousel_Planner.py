import streamlit as st

from agents.carousel_agent import analyze_carousel

st.set_page_config(
    page_title="Carousel Planner",
    page_icon="🎠",
    layout="wide"
)

st.title("🎠 Carousel Planner")

st.write(
    "Upload multiple photos and let the AI analyze each one."
)

uploaded_files = st.file_uploader(
    "Upload Carousel Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"{len(uploaded_files)} image(s) uploaded.")

    if st.button("Analyze Carousel"):

        progress_bar = st.progress(0)
        status = st.empty()

        results = analyze_carousel(uploaded_files)

        progress_bar.progress(100)
        status.success("Analysis Complete!")

        st.divider()

        for result in results:

            st.subheader(
                f"📷 Image {result['image_number']} - {result['filename']}"
            )

            analysis = result["analysis"]

            if isinstance(analysis, str) and analysis.startswith("❌"):
                st.error(analysis)
            else:
                st.markdown(analysis)

            st.divider()
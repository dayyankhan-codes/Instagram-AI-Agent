import streamlit as st

from agents.carousel_agent import analyze_carousel


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📷",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("🎠 Carousel Planner")

st.write(
    "Upload multiple photographs and receive AI-powered "
    "analysis for each image in your Instagram carousel."
)


st.divider()


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload Carousel Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)


# --------------------------------------------------
# IMAGE PREVIEW + ANALYSIS
# --------------------------------------------------

if uploaded_files:

    st.divider()

    left, right = st.columns([1, 1])


    # --------------------------------------------------
    # LEFT COLUMN — IMAGE PREVIEWS
    # --------------------------------------------------

    with left:

        st.subheader("📷 Uploaded Photos")

        st.caption(
            f"{len(uploaded_files)} image(s) selected"
        )

        for index, file in enumerate(uploaded_files):

            st.image(
                file,
                caption=f"{index + 1}. {file.name}",
                use_container_width=True
            )


    # --------------------------------------------------
    # RIGHT COLUMN — AI TOOL
    # --------------------------------------------------

    with right:

        st.subheader("🤖 AI Carousel Analysis")

        st.write(
            "The AI will analyze each photograph individually "
            "and provide photography feedback for every image "
            "in your carousel."
        )

        st.write(
            "Progress will update as each image is completed."
        )

        analyze_button = st.button(
            "Analyze Carousel",
            type="primary",
            use_container_width=True
        )


    # --------------------------------------------------
    # ANALYZE CAROUSEL
    # --------------------------------------------------

    if analyze_button:

        progress_bar = st.progress(0)

        status = st.empty()


        def update_progress(
            progress,
            current_image,
            total_images,
            filename
        ):

            percentage = int(progress * 100)

            progress_bar.progress(
                percentage
            )

            status.info(
                f"Analyzed image {current_image} "
                f"of {total_images}: {filename}"
            )


        status.info(
            f"Starting analysis of "
            f"{len(uploaded_files)} image(s)..."
        )


        try:

            results = analyze_carousel(
                uploaded_files,
                progress_callback=update_progress
            )


            progress_bar.progress(100)

            status.success(
                "Carousel analysis complete!"
            )


            st.session_state[
                "carousel_results"
            ] = results


            st.session_state[
                "carousel_filenames"
            ] = [
                file.name
                for file in uploaded_files
            ]


        except Exception as error:

            progress_bar.empty()

            status.error(
                f"An unexpected error occurred: {error}"
            )


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "carousel_results" in st.session_state:

    results = st.session_state[
        "carousel_results"
    ]

    st.divider()

    st.subheader("✨ Carousel Analysis Results")

    st.caption(
        f"{len(results)} image(s) analyzed"
    )


    for result in results:

        image_number = result.get(
            "image_number",
            "?"
        )

        filename = result.get(
            "filename",
            "Unknown Image"
        )

        analysis = result.get(
            "analysis",
            ""
        )


        # ----------------------------------------------
        # IMAGE RESULT
        # ----------------------------------------------

        with st.container(border=True):

            st.markdown(
                f"### 📷 Image {image_number}"
            )

            st.caption(
                filename
            )


            if (
                isinstance(analysis, str)
                and analysis.startswith("❌")
            ):

                st.error(
                    analysis
                )

            elif isinstance(analysis, str):

                st.markdown(
                    analysis
                )

            else:

                st.error(
                    "Unexpected response format received "
                    "from Gemini."
                )

                st.write(
                    analysis
                )
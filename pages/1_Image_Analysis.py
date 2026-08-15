import streamlit as st

from agents.image_analyzer import analyze_image


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

st.title("📷 Image Analysis")

st.write(
    "Upload a photograph and receive AI-powered feedback "
    "on its composition, lighting, colors, technical quality, "
    "and overall visual impact."
)


st.divider()


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Photo",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)


# --------------------------------------------------
# IMAGE PREVIEW + ANALYSIS
# --------------------------------------------------

if uploaded_file:

    st.divider()

    left, right = st.columns([1, 1])

    with left:

        st.subheader("📷 Original Photo")

        st.image(
            uploaded_file,
            caption=uploaded_file.name,
            use_container_width=True
        )


    with right:

        st.subheader("🤖 AI Image Analysis")

        st.write(
            "The AI will analyze the photograph and provide feedback "
            "on composition, lighting, colors, technical quality, "
            "visual strengths, and areas for improvement."
        )

        analyze_button = st.button(
            "Analyze Photo",
            type="primary",
            use_container_width=True
        )


    # --------------------------------------------------
    # GENERATE ANALYSIS
    # --------------------------------------------------

    if analyze_button:

        with st.spinner("Analyzing photograph..."):

            result = analyze_image(uploaded_file)

        st.session_state[
            "image_analysis_result"
        ] = result

        st.session_state[
            "image_analysis_filename"
        ] = uploaded_file.name


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "image_analysis_result" in st.session_state:

    result = st.session_state[
        "image_analysis_result"
    ]

    st.divider()

    st.subheader("✨ Image Analysis")

    st.caption(
        "Generated for: "
        f"{st.session_state.get('image_analysis_filename', 'Photo')}"
    )


    # --------------------------------------------------
    # ERROR HANDLING
    # --------------------------------------------------

    if isinstance(result, str) and result.startswith("❌"):

        st.error(result)

    elif isinstance(result, str):

        st.markdown(result)

    else:

        st.error(
            "Unexpected response format received from Gemini."
        )

        st.write(result)
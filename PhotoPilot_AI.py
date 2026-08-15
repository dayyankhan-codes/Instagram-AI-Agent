import streamlit as st


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📸",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("📸 PhotoPilot AI")

st.subheader(
    "Your AI-powered photography workspace"
)

st.write(
    "Analyze your photographs, plan Instagram carousels, "
    "generate Lightroom Classic editing recommendations, "
    "create captions, and discover music that matches "
    "your visual style."
)


st.divider()


# --------------------------------------------------
# FEATURE OVERVIEW
# --------------------------------------------------

st.header("✨ Photography Tools")


col1, col2 = st.columns(2)


with col1:

    with st.container(border=True):

        st.markdown("### 📷 Image Analysis")

        st.write(
            "Receive AI-powered feedback on composition, "
            "lighting, colors, technical quality, visual "
            "strengths, and areas for improvement."
        )


    with st.container(border=True):

        st.markdown("### 🎨 Lightroom Editor")

        st.write(
            "Generate custom Adobe Lightroom Classic "
            "recommendations with fixed values tailored "
            "specifically to your photograph."
        )


    with st.container(border=True):

        st.markdown("### 🎵 Music Suggestions")

        st.write(
            "Discover music recommendations that match "
            "the mood, atmosphere, and visual aesthetic "
            "of your photograph."
        )


with col2:

    with st.container(border=True):

        st.markdown("### 🎠 Carousel Planner")

        st.write(
            "Analyze multiple photographs individually "
            "and get AI-powered feedback for your "
            "Instagram carousel."
        )


    with st.container(border=True):

        st.markdown("### 📝 Caption Generator")

        st.write(
            "Generate multiple caption options based on "
            "your photograph, its subject, mood, and "
            "visual story."
        )


    with st.container(border=True):

        st.markdown("### ⚙️ Settings")

        st.write(
            "View your current AI configuration, test "
            "the Gemini connection, and manage your "
            "current session."
        )


st.divider()


# --------------------------------------------------
# GETTING STARTED
# --------------------------------------------------

st.header("🚀 Get Started")

st.info(
    "Choose a photography tool from the sidebar to begin."
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "PhotoPilot AI • Powered by Python, Streamlit and Google Gemini"
)
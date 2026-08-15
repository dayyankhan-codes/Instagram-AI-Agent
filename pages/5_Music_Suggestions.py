import streamlit as st

from agents.music_agent import generate_music_suggestions


st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📷",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("🎵 Music Suggestions")

st.write(
    "Upload a photograph and discover songs that match "
    "its mood, atmosphere, and visual aesthetic."
)


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Photo",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)


# --------------------------------------------------
# IMAGE PREVIEW + GENERATE BUTTON
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

        st.subheader("🎶 AI Music Suggestions")

        st.write(
            "The AI will analyze the photograph's mood, "
            "atmosphere, and aesthetic to recommend music "
            "that genuinely fits the image."
        )

        generate_button = st.button(
            "Generate Music Suggestions",
            type="primary",
            use_container_width=True
        )

    if generate_button:

        with st.spinner(
            "Analyzing photograph and finding matching music..."
        ):

            result = generate_music_suggestions(
                uploaded_file
            )

        st.session_state[
            "music_result"
        ] = result

        st.session_state[
            "music_filename"
        ] = uploaded_file.name


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "music_result" in st.session_state:

    result = st.session_state[
        "music_result"
    ]

    st.divider()

    st.subheader("🎵 Music Recommendations")

    st.caption(
        "Generated for: "
        f"{st.session_state.get('music_filename', 'Photo')}"
    )


    # ----------------------------------------------
    # ERROR HANDLING
    # ----------------------------------------------

    if isinstance(result, str):

        if result.startswith("❌"):

            st.error(result)

        else:

            st.error(
                "Gemini returned an unexpected response format."
            )

            with st.expander("Show Response"):

                st.code(
                    result,
                    language="text"
                )


    elif (
        isinstance(result, dict)
        and "error" in result
    ):

        st.error(
            result["error"]
        )

        with st.expander(
            "Show Gemini Response"
        ):

            st.code(
                result.get(
                    "raw_response",
                    ""
                ),
                language="text"
            )


    # ----------------------------------------------
    # MUSIC RESULTS
    # ----------------------------------------------

    elif isinstance(result, dict):

        image_mood = result.get(
            "image_mood",
            ""
        )

        if image_mood:

            st.markdown("### 🎨 Image Mood")

            st.info(image_mood)


        suggestions = result.get(
            "suggestions",
            []
        )

        if not suggestions:

            st.warning(
                "No music suggestions were returned."
            )

        else:

            for index, suggestion in enumerate(
                suggestions
            ):

                if not isinstance(
                    suggestion,
                    dict
                ):
                    continue

                song = suggestion.get(
                    "song",
                    "Unknown Song"
                )

                artist = suggestion.get(
                    "artist",
                    "Unknown Artist"
                )

                mood = suggestion.get(
                    "mood",
                    ""
                )

                why = suggestion.get(
                    "why",
                    ""
                )


                # ----------------------------------
                # SONG CARD
                # ----------------------------------

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"### {index + 1}. 🎵 {song}"
                    )

                    st.markdown(
                        f"**Artist:** {artist}"
                    )

                    if mood:

                        st.markdown(
                            f"**Mood:** {mood}"
                        )

                    if why:

                        st.markdown(
                            f"**Why it fits:** {why}"
                        )


    else:

        st.error(
            "Unexpected response format "
            "received from Gemini."
        )

        st.write(result)
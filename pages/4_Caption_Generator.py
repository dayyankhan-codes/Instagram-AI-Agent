import streamlit as st

from agents.caption_agent import generate_captions


st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📷",
    layout="wide"
)


st.title("📝 Caption Generator")

st.write(
    "Upload a photograph and generate multiple Instagram "
    "caption options based specifically on that image."
)


# ----------------------------------------------
# IMAGE UPLOAD
# ----------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Photo",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)


# ----------------------------------------------
# IMAGE PREVIEW AND GENERATE BUTTON
# ----------------------------------------------

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

        st.subheader("✨ AI Caption Generator")

        st.write(
            "The AI will analyze the actual photograph and "
            "generate 5 different caption styles."
        )

        generate_button = st.button(
            "Generate Captions",
            type="primary",
            use_container_width=True
        )

    if generate_button:

        with st.spinner(
            "Analyzing photograph and writing captions..."
        ):

            result = generate_captions(
                uploaded_file
            )

        st.session_state[
            "caption_result"
        ] = result

        st.session_state[
            "caption_filename"
        ] = uploaded_file.name


# ----------------------------------------------
# DISPLAY RESULTS
# ----------------------------------------------

if "caption_result" in st.session_state:

    result = st.session_state[
        "caption_result"
    ]

    st.divider()

    st.subheader("✨ Generated Captions")

    st.caption(
        "Generated for: "
        f"{st.session_state.get('caption_filename', 'Photo')}"
    )


    # ------------------------------------------
    # ERROR HANDLING
    # ------------------------------------------

    if isinstance(result, str):

        if result.startswith("❌"):

            st.error(result)

        else:

            st.error(
                "Gemini returned an unexpected response format."
            )

            with st.expander(
                "Show Response"
            ):

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


    # ------------------------------------------
    # CAPTIONS
    # ------------------------------------------

    elif isinstance(result, dict):

        captions = result.get(
            "captions",
            []
        )

        if not captions:

            st.warning(
                "No captions were returned."
            )

        else:

            for index, item in enumerate(
                captions
            ):

                style = item.get(
                    "style",
                    f"Caption {index + 1}"
                )

                caption = item.get(
                    "caption",
                    ""
                )

                st.markdown(
                    f"### {index + 1}. {style}"
                )

                st.text_area(
                    label=f"Caption {index + 1}",
                    value=caption,
                    height=130,
                    key=f"caption_{index}",
                    label_visibility="collapsed"
                )

                st.divider()


    else:

        st.error(
            "Unexpected response format received from Gemini."
        )

        st.write(result)
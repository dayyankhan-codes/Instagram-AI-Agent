import streamlit as st
import pandas as pd

from agents.lightroom_agent import generate_lightroom_recommendation


st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📷",
    layout="wide"
)


def format_value(value):
    """
    Format Lightroom values cleanly.
    """

    if isinstance(value, float):

        # Convert whole-number floats
        # Example: 45.0 -> 45
        if value.is_integer():
            return str(int(value))

        # Keep up to 2 decimal places
        formatted = f"{value:.2f}"

        return formatted.rstrip("0").rstrip(".")

    return str(value)


def settings_table(settings):
    """
    Display Lightroom settings as a clean
    Setting / Value table.
    """

    if not isinstance(settings, dict):
        return

    rows = []

    for name, value in settings.items():

        # Do not display explanation fields as settings
        if str(name).lower() in [
            "why",
            "explanation"
        ]:
            continue

        rows.append(
            {
                "Setting": (
                    str(name)
                    .replace("_", " ")
                    .title()
                ),
                "Value": format_value(value)
            }
        )

    if rows:

        df = pd.DataFrame(rows)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


def display_why(data, fallback=None):
    """
    Display explanation text.
    """

    why = None

    if isinstance(data, dict):

        why = data.get("why")

    if not why and fallback:

        why = fallback

    if why:

        st.markdown(
            f"**Why:** {why}"
        )


def display_standard_section(
    title,
    data,
    separate_why=None
):
    """
    Display a standard Lightroom section
    containing settings and an explanation.
    """

    st.markdown(f"## {title}")

    if not isinstance(data, dict):

        st.write(data)

        return

    settings_table(data)

    display_why(
        data,
        separate_why
    )


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("🎨 Lightroom Editor")

st.write(
    "Upload a photograph and generate custom "
    "Adobe Lightroom Classic settings specifically "
    "for that image."
)


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Photo",
    type=[
        "jpg",
        "jpeg",
        "png"
    ],
    accept_multiple_files=False
)


# --------------------------------------------------
# IMAGE PREVIEW + BUTTON
# --------------------------------------------------

if uploaded_file:

    st.divider()

    left, right = st.columns(
        [1, 1]
    )

    with left:

        st.subheader(
            "📷 Original Photo"
        )

        st.image(
            uploaded_file,
            caption=uploaded_file.name,
            use_container_width=True
        )

    with right:

        st.subheader(
            "🎨 AI Lightroom Editor"
        )

        st.write(
            "The AI will analyze the photograph "
            "and create fixed Lightroom Classic "
            "values."
        )

        analyze_button = st.button(
            "Generate Lightroom Settings",
            type="primary",
            use_container_width=True
        )

    if analyze_button:

        with st.spinner(
            "Analyzing photograph and creating "
            "Lightroom settings..."
        ):

            result = (
                generate_lightroom_recommendation(
                    uploaded_file
                )
            )

        st.session_state[
            "lightroom_result"
        ] = result

        st.session_state[
            "lightroom_filename"
        ] = uploaded_file.name


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "lightroom_result" in st.session_state:

    result = st.session_state[
        "lightroom_result"
    ]

    st.divider()

    st.subheader(
        "🎨 Lightroom Classic Recommendation"
    )

    st.caption(
        "Settings generated for: "
        f"{st.session_state.get('lightroom_filename', 'Photo')}"
    )


    # ----------------------------------------------
    # ERROR HANDLING
    # ----------------------------------------------

    if isinstance(result, str):

        if result.startswith("❌"):

            st.error(result)

        else:

            st.error(
                "Gemini returned an unexpected "
                "response format."
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


    elif isinstance(result, dict):


        # ------------------------------------------
        # BASIC
        # ------------------------------------------

        if "basic" in result:

            display_standard_section(
                "Basic",
                result["basic"],
                result.get("basic_why")
            )


        # ------------------------------------------
        # TONE CURVE
        # ------------------------------------------

        if "tone_curve" in result:

            display_standard_section(
                "Tone Curve",
                result["tone_curve"],
                result.get("tone_curve_why")
            )


        # ------------------------------------------
        # HSL
        # ------------------------------------------

        if "hsl" in result:

            st.markdown(
                "## HSL"
            )

            hsl = result["hsl"]

            if isinstance(hsl, dict):

                rows = []

                for color, values in hsl.items():

                    if not isinstance(
                        values,
                        dict
                    ):
                        continue

                    rows.append(
                        {
                            "Color": str(
                                color
                            ).title(),

                            "Hue": format_value(
                                values.get(
                                    "Hue",
                                    values.get(
                                        "hue",
                                        0
                                    )
                                )
                            ),

                            "Saturation": format_value(
                                values.get(
                                    "Saturation",
                                    values.get(
                                        "saturation",
                                        0
                                    )
                                )
                            ),

                            "Luminance": format_value(
                                values.get(
                                    "Luminance",
                                    values.get(
                                        "luminance",
                                        0
                                    )
                                )
                            )
                        }
                    )

                if rows:

                    hsl_df = pd.DataFrame(
                        rows
                    )

                    st.dataframe(
                        hsl_df,
                        use_container_width=True,
                        hide_index=True
                    )

            display_why(
                hsl,
                result.get(
                    "hsl_why"
                )
            )


        # ------------------------------------------
        # COLOR GRADING
        # ------------------------------------------

        if "color_grading" in result:

            st.markdown(
                "## Color Grading"
            )

            grading = result[
                "color_grading"
            ]

            if isinstance(
                grading,
                dict
            ):

                rows = []

                for name in [
                    "Shadows",
                    "Midtones",
                    "Highlights"
                ]:

                    values = grading.get(
                        name
                    )

                    if not isinstance(
                        values,
                        dict
                    ):
                        continue

                    rows.append(
                        {
                            "Range": name,

                            "Hue": format_value(
                                values.get(
                                    "Hue",
                                    values.get(
                                        "hue",
                                        0
                                    )
                                )
                            ),

                            "Saturation": format_value(
                                values.get(
                                    "Saturation",
                                    values.get(
                                        "saturation",
                                        0
                                    )
                                )
                            )
                        }
                    )

                if rows:

                    grading_df = pd.DataFrame(
                        rows
                    )

                    st.dataframe(
                        grading_df,
                        use_container_width=True,
                        hide_index=True
                    )


                if "Balance" in grading:

                    st.markdown(
                        "### Balance"
                    )

                    settings_table(
                        {
                            "Balance": grading[
                                "Balance"
                            ]
                        }
                    )

            display_why(
                grading,
                result.get(
                    "color_grading_why"
                )
            )


        # ------------------------------------------
        # DETAIL
        # ------------------------------------------

        if "detail" in result:

            display_standard_section(
                "Detail",
                result["detail"],
                result.get(
                    "detail_why"
                )
            )


        # ------------------------------------------
        # LENS CORRECTIONS
        # ------------------------------------------

        if "lens_corrections" in result:

            display_standard_section(
                "Lens Corrections",
                result[
                    "lens_corrections"
                ],
                result.get(
                    "lens_corrections_why"
                )
            )


        # ------------------------------------------
        # EFFECTS
        # ------------------------------------------

        if "effects" in result:

            display_standard_section(
                "Effects",
                result["effects"],
                result.get(
                    "effects_why"
                )
            )


        # ------------------------------------------
        # CALIBRATION
        # ------------------------------------------

        if "calibration" in result:

            display_standard_section(
                "Calibration",
                result["calibration"],
                result.get(
                    "calibration_why"
                )
            )


        # ------------------------------------------
        # MASKING
        # ------------------------------------------

        if "masking" in result:

            st.markdown(
                "## Masking"
            )

            masks = result[
                "masking"
            ]

            if not masks:

                st.info(
                    "No additional masks are "
                    "recommended for this photograph."
                )

            elif isinstance(
                masks,
                list
            ):

                for index, mask in enumerate(
                    masks
                ):

                    if not isinstance(
                        mask,
                        dict
                    ):
                        continue

                    mask_name = mask.get(
                        "name",
                        f"Mask {index + 1}"
                    )

                    st.markdown(
                        f"### Mask {index + 1} — "
                        f"{mask_name}"
                    )

                    mask_type = mask.get(
                        "mask_type"
                    )

                    if mask_type:

                        st.caption(
                            f"Mask Type: "
                            f"{mask_type}"
                        )

                    settings = mask.get(
                        "settings",
                        {}
                    )

                    settings_table(
                        settings
                    )

                    display_why(
                        mask
                    )


    else:

        st.error(
            "Unexpected response format "
            "received from Gemini."
        )

        st.write(result)
from PIL import Image
import io
import json

from services.gemini_service import ask_gemini
from services.prompt_loader import load_prompt

def prepare_image(uploaded_file):
    """
    Resize and optimize the uploaded image before sending it to Gemini.
    This reduces API processing time while preserving enough detail
    for photography analysis.
    """

    image = Image.open(uploaded_file)

    # Convert unsupported modes to RGB
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")

    # Limit image dimensions
    max_size = 1600

    image.thumbnail(
        (max_size, max_size)
    )

    # Save optimized version in memory
    buffer = io.BytesIO()

    image.save(
        buffer,
        format="JPEG",
        quality=85,
        optimize=True
    )

    buffer.seek(0)

    optimized_image = Image.open(buffer)

    return optimized_image


def generate_lightroom_recommendation(uploaded_file):

    prompt = load_prompt(
        "lightroom_recommendation.txt"
    )

    optimized_image = prepare_image(
        uploaded_file
    )

    response = ask_gemini(
        prompt,
        optimized_image
    )

    if isinstance(response, str):

        if response.startswith("❌"):
            return {
                "error": response
            }

        try:

            # Remove accidental markdown fences if Gemini adds them
            cleaned_response = response.strip()

            if cleaned_response.startswith("```json"):

                cleaned_response = cleaned_response.replace(
                    "```json",
                    "",
                    1
                )

            if cleaned_response.startswith("```"):

                cleaned_response = cleaned_response.replace(
                    "```",
                    "",
                    1
                )

            if cleaned_response.endswith("```"):

                cleaned_response = cleaned_response[:-3]

            return json.loads(
                cleaned_response.strip()
            )

        except json.JSONDecodeError:

            return {
                "error": "Gemini returned an invalid response format.",
                "raw_response": response
            }

    return response
from PIL import Image
import json

from services.gemini_service import ask_gemini
from services.prompt_loader import load_prompt
from services.knowledge_service import load_knowledge


def generate_captions(uploaded_file):
    """
    Analyze an uploaded image and generate
    Instagram caption suggestions.
    """

    image = Image.open(uploaded_file)

    prompt = load_prompt(
        "caption_generation.txt"
    )

    knowledge = load_knowledge()

    final_prompt = f"""
You are my professional Instagram photography assistant.

Use the following knowledge about the user and
their photography preferences when generating captions.

{knowledge}

{prompt}
"""

    response = ask_gemini(
        final_prompt,
        image
    )

    # Gemini service error
    if isinstance(response, str) and response.startswith("❌"):

        return {
            "error": response,
            "raw_response": response
        }

    # Parse JSON response
    try:

        return json.loads(response)

    except json.JSONDecodeError:

        # Handle occasional Markdown code fences
        cleaned_response = response.strip()

        if cleaned_response.startswith("```json"):

            cleaned_response = cleaned_response.replace(
                "```json",
                "",
                1
            )

            cleaned_response = cleaned_response.rstrip(
                "`"
            ).strip()

        try:

            return json.loads(
                cleaned_response
            )

        except json.JSONDecodeError:

            return {
                "error": (
                    "Gemini returned an invalid response format."
                ),
                "raw_response": response
            }
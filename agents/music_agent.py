from PIL import Image
import json

from services.gemini_service import ask_gemini
from services.prompt_loader import load_prompt
from services.knowledge_service import load_knowledge


def generate_music_suggestions(uploaded_file):
    """
    Analyze an uploaded photograph and generate
    music suggestions that match its mood and aesthetic.
    """

    image = Image.open(uploaded_file)

    prompt = load_prompt(
        "music_suggestions.txt"
    )

    knowledge = load_knowledge()

    final_prompt = f"""
You are my professional photography and Instagram content assistant.

Use the following knowledge when making music suggestions.

{knowledge}

{prompt}
"""

    response = ask_gemini(
        final_prompt,
        image
    )

    # Handle Gemini errors
    if isinstance(response, str) and response.startswith("❌"):

        return {
            "error": response,
            "raw_response": response
        }

    # Parse JSON
    try:

        return json.loads(response)

    except json.JSONDecodeError:

        cleaned_response = response.strip()

        # Handle occasional Markdown JSON fences
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

            return json.loads(cleaned_response)

        except json.JSONDecodeError:

            return {
                "error": (
                    "Gemini returned an invalid response format."
                ),
                "raw_response": response
            }
            
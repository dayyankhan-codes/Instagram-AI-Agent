import json

from PIL import Image

from services.gemini_service import ask_gemini
from services.prompt_loader import load_prompt
from services.knowledge_service import load_knowledge


def generate_lightroom_recommendation(uploaded_file):
    """
    Analyze an image and generate structured Lightroom Classic settings.
    """

    image = Image.open(uploaded_file)

    if image.mode != "RGB":
        image = image.convert("RGB")

    prompt = load_prompt("lightroom_recommendation.txt")
    knowledge = load_knowledge()

    final_prompt = f"""
You are my personal professional photography and Lightroom Classic assistant.

Use the photographer knowledge below only when relevant:

{knowledge}

Follow these instructions exactly:

{prompt}

Return ONLY valid JSON.
Do not use Markdown.
Do not use ```json.
Do not write anything before or after the JSON.
"""

    result = ask_gemini(
        final_prompt,
        image
    )

    if not isinstance(result, str):
        return result

    if result.startswith("❌"):
        return result

    # Remove accidental Markdown code fences if Gemini adds them.
    cleaned = result.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]

    if cleaned.startswith("```"):
        cleaned = cleaned[3:]

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError:
        return {
            "error": "Gemini returned an invalid JSON response.",
            "raw_response": result
        }
from PIL import Image

from services.gemini_service import ask_gemini
from services.knowledge_service import load_knowledge


def test_connection():
    return ask_gemini(
        "Reply only with: Gemini connection successful."
    )


def analyze_image(uploaded_file):

    image = Image.open(uploaded_file)

    with open(
        "prompts/image_analysis.txt",
        "r",
        encoding="utf-8"
    ) as file:

        prompt = file.read()

    knowledge = load_knowledge()

    final_prompt = f"""

You are my personal photography assistant.

Use the following knowledge while analyzing.

{knowledge}

{prompt}

"""

    return ask_gemini(final_prompt, image)
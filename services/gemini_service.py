from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

from config import MODEL_NAME

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt, image=None):
    """
    Sends a prompt (and optional image) to Gemini.
    Returns only the generated text.
    """

    contents = [prompt]

    if image is not None:
        contents.insert(0, image)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1500,
        )
    )

    if response.text:
        return response.text

    return "No response returned."
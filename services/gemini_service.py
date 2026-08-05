from google import genai
from dotenv import load_dotenv
import os
import time

from config import MODEL_NAME

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt, image=None):
    """
    Sends a request to Gemini.

    Automatically retries temporary server errors.

    Returns either:
        - response.text
        - friendly error message
    """

    max_retries = 3

    for attempt in range(max_retries):

        try:

            if image is None:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

            else:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=[prompt, image]
                )

            if response.text:
                return response.text

            return "⚠ Gemini returned an empty response."

        except Exception as e:

            print(f"Attempt {attempt+1} failed:")
            print(e)

            if attempt < max_retries - 1:

                wait = 2 ** attempt

                print(f"Retrying in {wait} seconds...")

                time.sleep(wait)

            else:

                return f"""
❌ Gemini is currently unavailable.

Please try again in a few moments.

Technical details:
{e}
"""
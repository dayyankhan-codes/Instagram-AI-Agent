from config import MODEL_NAME
from google import genai
from dotenv import load_dotenv
import os

print("Loading image_analyzer.py...")

load_dotenv()

print("Loading API key...")

api_key = os.getenv("GEMINI_API_KEY")

print("API key found:", api_key is not None)

client = genai.Client(api_key=api_key)

print("Gemini client created!")

def test_connection():
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents="Reply only with: Gemini connection successful."
        )

        return response.text

    except Exception as e:
        return f"Error:\n\n{e}"

from PIL import Image
from google.genai import types

def analyze_image(image_file):
    try:
        # Open and resize image
        image = Image.open(image_file)
        image.thumbnail((1600, 1600))

        # Send image to Gemini
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                image,
                "Describe the main subject of this image in one sentence."
            ],
            config=types.GenerateContentConfig(
                temperature=0,
                max_output_tokens=300,
            )
        )

        print("========== GEMINI RESPONSE ==========")
        print(response)
        print("=====================================")

        if response.text:
            return response.text
        else:
            return f"No text returned.\n\n{response}"

    except Exception as e:
        print("ERROR:", e)
        return str(e)      

    print("Response received!")

    return response.text
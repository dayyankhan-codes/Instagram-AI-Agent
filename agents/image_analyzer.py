from PIL import Image

from services.gemini_service import ask_gemini
from services.prompt_loader import load_prompt


def analyze_image(image_file):
    """
    Analyze one uploaded image.
    """

    image = Image.open(image_file)

    # Resize large images
    image.thumbnail((1600, 1600))

    # Load the prompt from file
    prompt = load_prompt("image_analysis.txt")

    # Ask Gemini
    result = ask_gemini(prompt, image)

    return result
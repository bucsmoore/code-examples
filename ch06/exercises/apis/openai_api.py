import datetime
import os
from base64 import b64decode

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # take environment variables from .env

client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))


def generate_image(prompt):
    image = None
    response = client.images.generate(
        model="dall-e-3", prompt=prompt, response_format="b64_json"
    )
    image_dict = response.data[0]
    image = b64decode(image_dict.b64_json)
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"images/{current_time}.webp"
    with open(file_path, "wb") as asset:
        asset.write(image)
    print(f"View your image here: {file_path}")


def main():
    prompt = input("Describe the image you would like me to generate:")
    prompt = prompt or "A teddy bear riding a dragon chasing a group of politicians"
    generate_image(prompt)


main()

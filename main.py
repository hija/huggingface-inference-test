from typing import Union
import requests
import dotenv
import os

import io
import base64
from PIL import Image

import traceback

dotenv.load_dotenv(dotenv_path=dotenv.find_dotenv())
API_URL = os.environ.get("HUGGINGFACE_INFERENCE_URL", None)
BEARER_TOKEN = os.environ.get("HUGGINGFACE_BEARER_TOKEN", None)

if not API_URL or API_URL == "https://YOUR_INFERENCE_URL_HERE.huggingface.cloud":
    raise ValueError("Please set the HUGGINGFACE_INFERENCE_URL in your .env file")
if not BEARER_TOKEN or BEARER_TOKEN == "INSERT_YOUR_TOKEN_HERE":
    raise ValueError("Please set the BEARER_TOKEN in your .env file")


def get_image(image_query) -> Union[Image.Image, None]:
    payload = {"inputs": image_query}

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        convertedbytes = base64.b64decode(response.content)
        return Image.open(io.BytesIO(convertedbytes))
    except:
        traceback.print_exc()
        return None


print(
    get_image("A hacker sitting in front of a computer with a guy fawkes mask").show()
)

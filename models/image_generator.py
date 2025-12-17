import os
import requests
from PIL import Image
from io import BytesIO

class ImageGenerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
        self.headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}"
        }

    def generate(self, prompt, style, steps=20, guidance=7.5):
        payload = {
            "inputs": f"{prompt}, {style} style",
            "options": {"wait_for_model": True}
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=120
        )

        if response.status_code != 200:
            raise RuntimeError(response.text)

        return Image.open(BytesIO(response.content))

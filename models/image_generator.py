import requests
from PIL import Image
from io import BytesIO

class ImageGenerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
        self.headers = {
            "Authorization": "Bearer YOUR_HF_TOKEN"
        }

    def generate(self, prompt, style, steps, guidance):
        full_prompt = f"{prompt}, {style} style, ultra detailed, cinematic lighting"

        payload = {
            "inputs": full_prompt
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=60
        )

        image = Image.open(BytesIO(response.content))
        return image

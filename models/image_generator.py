import os
import requests
from PIL import Image
from io import BytesIO

class ImageGenerator:
    def __init__(self):
        self.api_url = (
            "https://router.huggingface.co/hf-inference/models/"
            "runwayml/stable-diffusion-v1-5"
        )

        self.headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
            "Accept": "image/png"
        }

    def generate(self, prompt, style, steps, guidance):
        payload = {
            "inputs": f"{prompt}, {style} style, high quality, ultra detailed",
            "parameters": {
                "num_inference_steps": steps,
                "guidance_scale": guidance
            }
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=180
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"HF API Error {response.status_code}: {response.text}"
            )

        return Image.open(BytesIO(response.content))

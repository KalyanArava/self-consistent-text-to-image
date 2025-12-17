import os
import requests
from PIL import Image
from io import BytesIO

class ImageGenerator:
    def __init__(self):
        self.api_url = (
            "https://router.huggingface.co/hf-inference/models/"
            "stabilityai/stable-diffusion-2-1"
        )

        self.headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt, style, steps=20, guidance=7.5):
        payload = {
            "inputs": f"{prompt}, {style} style",
            "parameters": {
                "num_inference_steps": steps,
                "guidance_scale": guidance
            },
            "options": {
                "wait_for_model": True
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

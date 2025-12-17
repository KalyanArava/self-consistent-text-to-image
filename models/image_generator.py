import os
import requests
from PIL import Image
from io import BytesIO

class ImageGenerator:
    def __init__(self):
        self.token = os.getenv("HF_TOKEN")
        if not self.token:
            raise ValueError("HF_TOKEN not set")

        # ✅ STABLE DIFFUSION MODEL
        self.model_id = "stabilityai/stable-diffusion-2-1"

        # ✅ NEW HF ROUTER ENDPOINT (THIS FIXES 404)
        self.api_url = (
            f"https://router.huggingface.co/hf-inference/models/{self.model_id}"
        )

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt, style, steps, guidance):
        full_prompt = f"{prompt}, {style} style, high quality, ultra detailed"

        payload = {
            "inputs": full_prompt,
            "parameters": {
                "num_inference_steps": int(steps),
                "guidance_scale": float(guidance)
            }
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=300
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"HF API Error {response.status_code}: {response.text}"
            )

        return Image.open(BytesIO(response.content))

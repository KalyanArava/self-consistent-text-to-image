import requests
from PIL import Image
from io import BytesIO

class ImageGenerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/stabilityai/sd-turbo"
        self.headers = {
            "Authorization": "Bearer YOUR_HF_TOKEN"
        }

    def generate(self, prompt, style, steps, guidance):
        full_prompt = f"{prompt}, {style} style, high quality, detailed"

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={
                "inputs": full_prompt,
                "parameters": {
                    "guidance_scale": guidance,
                    "num_inference_steps": steps
                }
            },
            timeout=120
        )

        if response.status_code != 200:
            raise RuntimeError(f"HF API error: {response.text}")

        content_type = response.headers.get("content-type", "")

        # 🚨 THIS IS THE KEY FIX
        if not content_type.startswith("image/"):
            raise RuntimeError(
                "⚠️ Model is busy or loading.\n"
                "Please wait 20–30 seconds and click Generate again."
            )

        return Image.open(BytesIO(response.content)).convert("RGB")

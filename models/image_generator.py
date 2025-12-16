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
            timeout=120
        )

        # ❌ API error
        if response.status_code != 200:
            raise RuntimeError(
                f"HuggingFace API error {response.status_code}: {response.text}"
            )

        # ❌ Model loading / JSON response
        content_type = response.headers.get("content-type", "")
        if "image" not in content_type:
            raise RuntimeError(
                "Model is loading or API limit reached. Please try again in 30–60 seconds."
            )

        # ✅ Valid image
        return Image.open(BytesIO(response.content))

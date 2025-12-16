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

        payload = {"inputs": full_prompt}

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=120
        )

        # ❌ HTTP error
        if response.status_code != 200:
            raise RuntimeError(
                f"API error {response.status_code}: {response.text}"
            )

        # ❌ JSON response (model loading / error)
        if response.headers.get("content-type", "").startswith("application/json"):
            error_msg = response.json().get("error", "Unknown API error")
            raise RuntimeError(
                f"Model not ready: {error_msg}\nPlease wait 30–60 seconds and try again."
            )

        # ❌ Empty response
        if not response.content:
            raise RuntimeError("Empty response from model.")

        # ✅ Valid image
        try:
            return Image.open(BytesIO(response.content)).convert("RGB")
        except Exception:
            raise RuntimeError(
                "Received non-image data from API. Try again in a few seconds."
            )

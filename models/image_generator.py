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

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={"inputs": full_prompt},
            timeout=120
        )

        # ❌ API failed
        if response.status_code != 200:
            raise RuntimeError(
                f"HF API error {response.status_code}: {response.text}"
            )

        content_type = response.headers.get("content-type", "")

        # ❌ Model loading / error / HTML page
        if not content_type.startswith("image/"):
            raise RuntimeError(
                "Model is loading or rate-limited.\n"
                "Please wait 30–60 seconds and click Generate again."
            )

        # ❌ Empty bytes
        if len(response.content) < 1000:
            raise RuntimeError("Received empty image data.")

        # ✅ Safe to load
        return Image.open(BytesIO(response.content)).convert("RGB")

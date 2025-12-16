import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class ImageGenerator:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            use_auth_token=os.getenv("HF_TOKEN")
        )

        self.pipe.to(self.device)

        # Optimizations
        self.pipe.enable_attention_slicing()
        if self.device == "cpu":
            self.pipe.enable_sequential_cpu_offload()

    def generate(self, prompt, style, steps=18, guidance=7.5):
        full_prompt = f"{prompt}, {style} style, ultra-detailed, cinematic lighting, sharp focus"

        image = self.pipe(
            prompt=full_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=512,
            width=512
        ).images[0]

        return image

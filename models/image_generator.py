import torch
from diffusers import StableDiffusionPipeline


class ImageGenerator:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )

        self.pipe = self.pipe.to(self.device)

        if self.device == "cpu":
            self.pipe.enable_attention_slicing()

    def generate(self, prompt, style, steps=20, guidance=7.5):
        styled_prompt = f"{prompt}, {style}"

        image = self.pipe(
            prompt=styled_prompt,
            num_inference_steps=int(steps),
            guidance_scale=float(guidance),
            height=512,
            width=512
        ).images[0]

        return image

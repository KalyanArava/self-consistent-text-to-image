import torch
from diffusers import StableDiffusionPipeline

class ImageGenerator:
    def __init__(self):
        self.device = "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32
        ).to(self.device)

        self.pipe.enable_attention_slicing()

    def generate(self, prompt, style, steps=18, guidance=7.5):
        style_prompts = {
            "Cinematic": "cinematic lighting, dramatic shadows, ultra-detailed, film still, professional color grading",
            "Portrait": "sharp facial features, soft lighting, DSLR photo, 85mm lens, shallow depth of field",
            "Anime": "anime style, vibrant colors, clean line art, studio ghibli, high detail",
            "Landscape": "wide angle, epic scenery, natural lighting, HDR, ultra realistic",
            "Product": "studio lighting, clean background, sharp focus, commercial photography",
            "Fantasy": "fantasy art, magical lighting, epic atmosphere, concept art",
        }

        final_prompt = f"{prompt}, {style_prompts.get(style, '')}"

        image = self.pipe(
            prompt=final_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=512,
            width=512
        ).images[0]

        return image

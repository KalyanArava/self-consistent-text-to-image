import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image


class ConsistencyChecker:
    def __init__(self, device="cpu"):
        self.device = device
        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        ).to(device)

        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

    def score(self, text_prompt: str, image: Image.Image) -> float:
        """
        Computes CLIP cosine similarity between text and image
        """

        inputs = self.processor(
            text=[text_prompt],
            images=image,
            return_tensors="pt",
            padding=True
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)

        image_embeds = outputs.image_embeds
        text_embeds = outputs.text_embeds

        # Normalize
        image_embeds = image_embeds / image_embeds.norm(dim=-1, keepdim=True)
        text_embeds = text_embeds / text_embeds.norm(dim=-1, keepdim=True)

        # Cosine similarity
        similarity = (image_embeds * text_embeds).sum().item()

        return similarity

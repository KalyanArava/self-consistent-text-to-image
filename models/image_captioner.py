import torch
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageCaptioner:
    """
    Generates caption from generated image
    """

    def __init__(self):
        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

    def caption(self, image):
        inputs = self.processor(image, return_tensors="pt")

        with torch.no_grad():
            out = self.model.generate(**inputs)

        caption = self.processor.decode(
            out[0],
            skip_special_tokens=True
        )
        return caption

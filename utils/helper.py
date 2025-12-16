from PIL import ImageEnhance

def enhance_image(image):
    image = ImageEnhance.Contrast(image).enhance(1.25)
    image = ImageEnhance.Color(image).enhance(1.3)
    image = ImageEnhance.Sharpness(image).enhance(1.2)
    return image

from PIL import Image, ImageEnhance

def upscale_and_enhance(image):
    # ---------- UPSCALE ----------
    w, h = image.size
    image = image.resize((w * 2, h * 2), Image.LANCZOS)

    # ---------- SHARPNESS ----------
    sharpener = ImageEnhance.Sharpness(image)
    image = sharpener.enhance(1.4)

    # ---------- CONTRAST ----------
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(1.15)

    # ---------- COLOR ----------
    color = ImageEnhance.Color(image)
    image = color.enhance(1.2)

    return image

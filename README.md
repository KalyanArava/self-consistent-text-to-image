# 🎨 Self-Consistent Text-to-Image Generation System

A deep learning–based application that generates high-quality images from text prompts and verifies their semantic consistency using multimodal models.  
This project is designed as an **academic / final-year research project** with a modern UI and deployment support.

---

## 🚀 Project Overview

Text-to-image models often generate visually appealing images that may **not fully match the input prompt**.  
This project solves that problem by introducing a **self-consistency loop**:

1. Generate image from text
2. Generate caption from image
3. Measure similarity between original prompt and generated caption
4. Display consistency score to the user

---

## ✨ Key Features

- 🖼️ **Text → Image Generation** (Stable Diffusion)
- 📝 **Automatic Image Captioning**
- 📊 **Text–Image Consistency Scoring** (CLIP)
- 🎛️ **Midjourney / DALL·E–style UI** (Streamlit)
- ⚡ Optimized for **CPU & GPU**
- ☁️ Deployable on **Streamlit Cloud**
- 📁 Clean, modular project structure

---

## 🧠 Technologies Used

| Category | Tools |
|--------|------|
| Language | Python 3.10+ |
| UI | Streamlit |
| Image Generation | Stable Diffusion (Diffusers) |
| Captioning | Transformers |
| Consistency Check | CLIP |
| Deep Learning | PyTorch |
| Deployment | Streamlit Cloud |

---

## 📂 Project Structure

```text
Self_Consistent_Text_to_Image/
│
├── app.py                    # Main Streamlit app
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
│
├── models/
│   └── image_generator.py    # Image generation logic
│
├── utils/
│   └── image_enhancer.py     # Optional image enhancement
│
└── outputs/
    └── generated_images/     # Saved results

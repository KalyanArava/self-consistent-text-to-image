import os
import streamlit as st
from models.image_generator import ImageGenerator

st.set_page_config(page_title="Self-Consistent Text-to-Image", layout="wide")

if "HF_TOKEN" not in os.environ:
    st.error("❌ HF_TOKEN not found. Add it in Streamlit → Settings → Secrets")
    st.stop()

st.title("🎨 Self-Consistent Text-to-Image Generator")

@st.cache_resource
def load_model():
    return ImageGenerator()

generator = load_model()
st.success("✅ Model ready (Hugging Face API)")

st.sidebar.header("🎛 Settings")
style = st.sidebar.selectbox(
    "Style",
    ["Cinematic", "Portrait", "Anime", "Landscape", "Fantasy"]
)

prompt = st.text_area(
    "✍️ Prompt",
    height=120,
    placeholder="A futuristic city at night with neon lights"
)

if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        with st.spinner("🎨 Generating image (10–20s)..."):
            try:
                image = generator.generate(prompt, style)
                st.image(image, use_container_width=True)
            except Exception as e:
                st.error(str(e))

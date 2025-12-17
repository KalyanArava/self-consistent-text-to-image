import os
import streamlit as st
from models.image_generator import ImageGenerator

st.set_page_config(
    page_title="Self Consistent Text to Image",
    layout="wide"
)

st.title("🎨 Self-Consistent Text-to-Image Generator")

# ---- CHECK TOKEN ----
if "HF_TOKEN" not in os.environ:
    st.error("❌ HF_TOKEN not found. Add it in Streamlit → Settings → Secrets")
    st.stop()

# ---- LOAD MODEL ----
@st.cache_resource
def load_model():
    return ImageGenerator()

generator = load_model()
st.success("✅ Model ready (Hugging Face Router)")

# ---- SIDEBAR ----
st.sidebar.header("⚙ Settings")

style = st.sidebar.selectbox(
    "🎨 Style",
    ["Cinematic", "Anime", "Portrait", "Fantasy", "Landscape"]
)

steps = st.sidebar.slider("🌀 Steps", 10, 30, 20)
guidance = st.sidebar.slider("🎯 Guidance", 5.0, 12.0, 7.5)

# ---- PROMPT ----
prompt = st.text_area(
    "✍ Prompt",
    placeholder="A fantasy dragon flying over a medieval castle, epic lighting",
    height=120
)

# ---- GENERATE ----
if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        try:
            with st.spinner("🎨 Generating image (first run may take ~1 min)..."):
                image = generator.generate(
                    prompt=prompt,
                    style=style,
                    steps=steps,
                    guidance=guidance
                )

            st.image(image, use_container_width=True)

        except Exception as e:
            st.error(str(e))

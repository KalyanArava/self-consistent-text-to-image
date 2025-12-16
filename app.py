import streamlit as st
from models.image_generator import ImageGenerator
from utils.image_enhancer import upscale_and_enhance
from io import BytesIO

st.set_page_config(
    page_title="AI Image Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #6e40c9, #b5179e);
    color: white;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    return ImageGenerator()

generator = load_model()

# ---------- SIDEBAR ----------
st.sidebar.markdown("## 🎛 Settings")

style = st.sidebar.selectbox(
    "🎨 Style",
    ["Cinematic", "Portrait", "Anime", "Landscape", "Product", "Fantasy"]
)

steps = st.sidebar.slider("🌀 Steps", 10, 30, 18)
guidance = st.sidebar.slider("🎯 Guidance", 5.0, 12.0, 7.5)

# ---------- MAIN ----------
st.markdown("# 🖼 AI Image Generator")
st.markdown("### Midjourney / DALL·E–style")

prompt = st.text_area(
    "✍️ Prompt",
    height=120,
    placeholder="A futuristic city at night with neon lights"
)

generate = st.button("🚀 Generate")

if generate and prompt.strip():
    with st.spinner("🎨 Generating image..."):
        image = generator.generate(prompt, style, steps, guidance)

    st.session_state["image"] = image
    st.image(image, caption="Generated Image", use_container_width=True)

elif generate:
    st.warning("Please enter a prompt.")

# ---------- UPSCALE ----------
if "image" in st.session_state:
    st.markdown("## ✨ Enhance Image")

    if st.button("🔍 Upscale & Enhance"):
        with st.spinner("🚀 Enhancing quality..."):
            enhanced = upscale_and_enhance(st.session_state["image"])

        st.image(enhanced, caption="Enhanced Image", use_container_width=True)

        # Download
        buffer = BytesIO()
        enhanced.save(buffer, format="PNG")

        st.download_button(
            "⬇ Download Enhanced Image",
            data=buffer.getvalue(),
            file_name="enhanced.png",
            mime="image/png"
        )

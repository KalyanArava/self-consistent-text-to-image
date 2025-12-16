import streamlit as st
from models.image_generator import ImageGenerator
from io import BytesIO

st.set_page_config(
    page_title="Self Consistent Text to Image",
    layout="wide"
)

st.title("Self-Consistent Text-to-Image Generator")

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
def load_models():
    return ImageGenerator()

generator = load_models()
st.success("✅ Model loaded successfully")

# ---------- SIDEBAR ----------
st.sidebar.markdown("## 🎛 Settings")

style = st.sidebar.selectbox(
    "🎨 Style",
    ["Cinematic", "Portrait", "Anime", "Landscape", "Product", "Fantasy"]
)

steps = st.sidebar.slider("🌀 Steps", 10, 30, 18)
guidance = st.sidebar.slider("🎯 Guidance", 5.0, 12.0, 7.5)

# ---------- MAIN ----------
st.markdown("# 🎨 AI Image Generator")
st.markdown("### K–style")

prompt = st.text_area(
    "✍️ Prompt",
    height=120,
    placeholder="A futuristic city at night with neon lights"
)

generate = st.button("🚀 Generate")

if generate and prompt.strip():
    try:
        with st.spinner("🎨 Generating image (first run may take ~1 minute)..."):
            image = generator.generate(prompt, style, steps, guidance)

        st.session_state["image"] = image
        st.image(image, caption="Generated Image", use_container_width=True)

    except Exception as e:
        st.warning(str(e))

elif generate:
    st.warning("Please enter a prompt.")

import os
import streamlit as st
from models.image_generator import ImageGenerator

# --------------------------------------------------
# STREAMLIT PAGE CONFIG (MUST BE FIRST STREAMLIT CALL)
# --------------------------------------------------
st.set_page_config(
    page_title="Self Consistent Text to Image",
    layout="wide"
)

# --------------------------------------------------
# LOAD HF TOKEN (STREAMLIT CLOUD SAFE)
# --------------------------------------------------
HF_TOKEN = None

if "HF_TOKEN" in st.secrets:
    HF_TOKEN = st.secrets["HF_TOKEN"]
    os.environ["HF_TOKEN"] = HF_TOKEN
else:
    st.error("❌ HF_TOKEN not found. Add it in Streamlit Cloud → Settings → Secrets")
    st.stop()

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🎨 Self-Consistent Text-to-Image Generator")

# --------------------------------------------------
# CUSTOM STYLE
# --------------------------------------------------
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

# --------------------------------------------------
# LOAD MODEL (CACHED)
# --------------------------------------------------
@st.cache_resource(show_spinner=True)
def load_model():
    return ImageGenerator()

generator = load_model()
st.success("✅ Model loaded successfully")

# --------------------------------------------------
# SIDEBAR CONTROLS
# --------------------------------------------------
st.sidebar.markdown("## 🎛 Settings")

style = st.sidebar.selectbox(
    "🎨 Style",
    ["Cinematic", "Portrait", "Anime", "Landscape", "Product", "Fantasy"]
)

steps = st.sidebar.slider("🌀 Steps", 10, 30, 18)
guidance = st.sidebar.slider("🎯 Guidance", 5.0, 12.0, 7.5)

# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
st.markdown("## 🖼 AI Image Generator")

prompt = st.text_area(
    "✍️ Prompt",
    height=120,
    placeholder="A futuristic city at night with neon lights"
)

generate = st.button("🚀 Generate")

# --------------------------------------------------
# GENERATE IMAGE
# --------------------------------------------------
if generate:
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt.")
    else:
        try:
            with st.spinner("🎨 Generating image (first run may take 3–5 minutes on Streamlit Cloud)…"):
                image = generator.generate(
                    prompt=prompt,
                    style=style,
                    steps=steps,
                    guidance=guidance
                )

            st.session_state["image"] = image
            st.image(image, caption="Generated Image", use_container_width=True)

        except Exception as e:
            st.error("❌ Image generation failed")
            st.exception(e)

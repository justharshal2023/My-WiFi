import streamlit as st
import streamlit.components.v1 as components
import os, base64, re

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="For My Love 💕",
    page_icon="🌹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide all Streamlit chrome ─────────────────────────────────────────────────
st.markdown("""
<style>
    #MainMenu, header, footer, .stAppDeployButton { visibility: hidden; display: none; }
    [data-testid="collapsedControl"] { display: none; }
    section[data-testid="stSidebar"] { display: none; }
    .stApp { margin: 0 !important; padding: 0 !important; }
    .block-container, .stMainBlockContainer { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    iframe { display: block; border: none; }
</style>
""", unsafe_allow_html=True)

# ── Helper: convert any local image path → base64 data URL ───────────────────
def img_to_data_url(img_path: str) -> str | None:
    if not os.path.isfile(img_path):
        return None
    ext = os.path.splitext(img_path)[1].lower().lstrip(".")
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg",
            "png": "image/png", "gif": "image/gif",
            "webp": "image/webp"}.get(ext, "image/jpeg")
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

# ── Helper: replace <img src="filename"> with base64 inline version ───────────
def embed_images(html: str, base_dir: str) -> str:
    """
    Finds every <img src="..."> in the HTML.
    If the src looks like a local filename (not http/data),
    resolves it relative to base_dir and replaces with a base64 data URL.
    """
    def replace_src(match):
        full_tag = match.group(0)
        src = match.group(1)
        # Skip already-embedded or remote images
        if src.startswith("data:") or src.startswith("http"):
            return full_tag
        # Try to find the file relative to base_dir
        img_path = os.path.join(base_dir, src)
        data_url = img_to_data_url(img_path)
        if data_url:
            return full_tag.replace(src, data_url)
        else:
            st.warning(f"⚠️ Image not found: {src}  →  Expected at: {img_path}")
            return full_tag

    pattern = r'<img[^>]*\ssrc=["\']([^"\']+)["\'][^>]*>'
    return re.sub(pattern, replace_src, html, flags=re.IGNORECASE)

# ── Load HTML ─────────────────────────────────────────────────────────────────
base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "love.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# ── Embed all local images as base64 ─────────────────────────────────────────
html_content = embed_images(html_content, base_dir)

# ── Render ────────────────────────────────────────────────────────────────────
components.html(html_content, height=900, scrolling=True)

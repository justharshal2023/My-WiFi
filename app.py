import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="wide")

base_path = os.path.dirname(__file__)

# --- CSS ---
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #ff9a9e, #fecfef);
    overflow: hidden;
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 20px;
    animation: floatUp 6s linear infinite;
    color: #ff4d6d;
}
@keyframes floatUp {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(-100vh); opacity: 0; }
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: white;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: transparent;
    padding: 5px;
    text-align: center;
}

/* Remove image border/spacing */
img {
    border-radius: 12px;
    margin: 0px !important;
    padding: 0px !important;
}

/* Quotes */
.quote {
    font-size: 14px;
    color: white;
    margin-top: 6px;
}
</style>
""", unsafe_allow_html=True)

# --- Floating hearts ---
for i in range(15):
    st.markdown(f'<div class="heart" style="left:{i*7}%;">💖</div>', unsafe_allow_html=True)

# Session
if "open" not in st.session_state:
    st.session_state.open = False

# Intro
if not st.session_state.open:
    st.markdown('<div class="title">💖 Hey You 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">I made something special just for you...</div>', unsafe_allow_html=True)

    if st.button("✨ Open Your Surprise ✨"):
        st.session_state.open = True
        st.rerun()

else:
    st.markdown('<div class="title">For My Love ❤️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Every moment with you is magic ✨</div>', unsafe_allow_html=True)

    # Load images
    def load_img(name, rotate=False):
        img = Image.open(os.path.join(base_path, name))
        if rotate:
            img = img.rotate(90, expand=True)  # anticlockwise
        return img

    images = [
        (load_img("img1.jpeg"), "💫 You changed my world."),
        (load_img("img2.jpeg", True), "🌸 You are my peace."),
        (load_img("img3.jpeg"), "💖 Your smile = happiness."),
        (load_img("img4.jpeg", True), "🌹 My favorite person."),
        (load_img("img5.jpeg", True), "✨ Forever with you.")
    ]

    # Layout (centered)
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image(images[0][0], width=180)
        st.markdown(f'<div class="quote">{images[0][1]}</div>', unsafe_allow_html=True)

        st.image(images[3][0], width=180)
        st.markdown(f'<div class="quote">{images[3][1]}</div>', unsafe_allow_html=True)

    with col2:
        st.image(images[1][0], width=180)
        st.markdown(f'<div class="quote">{images[1][1]}</div>', unsafe_allow_html=True)

        st.image(images[4][0], width=180)
        st.markdown(f'<div class="quote">{images[4][1]}</div>', unsafe_allow_html=True)

    with col3:
        st.image(images[2][0], width=180)
        st.markdown(f'<div class="quote">{images[2][1]}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💌 One Last Surprise"):
        st.balloons()
        st.success("I love you more than anything ❤️")

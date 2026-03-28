import streamlit as st
import time
import os

st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="wide")

base_path = os.path.dirname(__file__)

# CSS
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ff9a9e, #fad0c4);
}
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: white;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: white;
    margin-bottom: 20px;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    text-align: center;
}
.quote {
    font-size: 14px;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# Session state
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

# Intro
if not st.session_state.unlocked:
    st.markdown('<div class="title">💖 Hey You 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">I made something special just for you...</div>', unsafe_allow_html=True)

    if st.button("✨ Open Your Surprise ✨"):
        with st.spinner("Opening... 💕"):
            time.sleep(2)
        st.session_state.unlocked = True
        st.rerun()

else:
    st.markdown('<div class="title">For My Love ❤️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Every moment with you is magic ✨</div>', unsafe_allow_html=True)

    # Create grid placeholders (2 rows)
    row1 = st.columns(3)
    row2 = st.columns(2)

    placeholders = [
        row1[0].empty(),
        row1[1].empty(),
        row1[2].empty(),
        row2[0].empty(),
        row2[1].empty()
    ]

    images = [
        ("img1.jpeg", "💫 You walked into my life and made everything brighter."),
        ("img2.jpeg", "🌸 You are my peace."),
        ("img3.jpeg", "💖 Your smile is my favorite."),
        ("img4.jpeg", "🌹 You are my magic."),
        ("img5.jpeg", "✨ My today & all my tomorrows.")
    ]

    # Sequential reveal
    for i, (img, quote) in enumerate(images):
        with placeholders[i]:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            # Portrait vs landscape sizing
            if i in [0, 2]:  # portrait images
                st.image(os.path.join(base_path, img), width=180)
            else:  # landscape images
                st.image(os.path.join(base_path, img), width=250)

            st.markdown(f'<div class="quote">{quote}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        time.sleep(1.2)  # delay for animation

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💌 One Last Surprise"):
        st.balloons()
        st.success("I love you more than anything ❤️")

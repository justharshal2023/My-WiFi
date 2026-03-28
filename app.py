import streamlit as st
import os

st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="wide")

base_path = os.path.dirname(__file__)

# CSS (animation + layout)
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ff9a9e, #fad0c4);
}
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
.card {
    background: white;
    padding: 10px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.2);

    opacity: 0;
    animation: fadeIn 1s forwards;
}
.card:nth-child(1) { animation-delay: 0.5s; }
.card:nth-child(2) { animation-delay: 1s; }
.card:nth-child(3) { animation-delay: 1.5s; }
.card:nth-child(4) { animation-delay: 2s; }
.card:nth-child(5) { animation-delay: 2.5s; }

@keyframes fadeIn {
    to { opacity: 1; }
}

.quote {
    font-size: 13px;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# Session state
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

    # Grid layout (fits screen)
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    images = [
        ("img1.jpeg", "💫 You changed my world."),
        ("img2.jpeg", "🌸 You are my peace."),
        ("img3.jpeg", "💖 Your smile = happiness."),
        ("img4.jpeg", "🌹 My favorite person."),
        ("img5.jpeg", "✨ Forever with you.")
    ]

    cols = [col1, col2, col3, col4, col5]

    for i, ((img, quote), col) in enumerate(zip(images, cols)):
        with col:
            st.markdown(f'<div class="card">', unsafe_allow_html=True)

            path = os.path.join(base_path, img)

            # Smaller sizing
            if i in [0, 2]:  # portrait
                st.image(path, width=160)
            else:  # landscape
                st.image(path, width=220)

            st.markdown(f'<div class="quote">{quote}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💌 One Last Surprise"):
        st.balloons()
        st.success("I love you more than anything ❤️")

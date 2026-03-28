import streamlit as st
import os
import base64

st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="wide")

base_path = os.path.dirname(__file__)

# Function to encode image
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# CSS
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
.container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
}
.card {
    background: white;
    padding: 12px;
    border-radius: 18px;
    width: 200px;
    text-align: center;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);

    opacity: 0;
    transform: translateY(20px);
    animation: fadeUp 1s forwards;
}
.card:nth-child(1) { animation-delay: 0.5s; }
.card:nth-child(2) { animation-delay: 1s; }
.card:nth-child(3) { animation-delay: 1.5s; }
.card:nth-child(4) { animation-delay: 2s; }
.card:nth-child(5) { animation-delay: 2.5s; }

@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.quote {
    font-size: 13px;
    margin-top: 6px;
}
</style>
""", unsafe_allow_html=True)

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

    images = [
        ("img1.jpeg", "💫 You changed my world."),
        ("img2.jpeg", "🌸 You are my peace."),
        ("img3.jpeg", "💖 Your smile = happiness."),
        ("img4.jpeg", "🌹 My favorite person."),
        ("img5.jpeg", "✨ Forever with you.")
    ]

    html = '<div class="container">'

    for img, quote in images:
        path = os.path.join(base_path, img)
        encoded = get_base64(path)

        html += f"""
        <div class="card">
            <img src="data:image/jpeg;base64,{encoded}" width="180">
            <div class="quote">{quote}</div>
        </div>
        """

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("💌 One Last Surprise"):
        st.balloons()
        st.success("I love you more than anything ❤️")

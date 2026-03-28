import streamlit as st
import time

# Page config
st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="wide")

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ff9a9e, #fad0c4);
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
    animation: fadeIn 2s ease-in;
}
.subtitle {
    text-align: center;
    font-size: 22px;
    color: white;
    margin-bottom: 30px;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 30px;
    animation: slideUp 1.5s ease;
    text-align: center;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
@keyframes slideUp {
    from {transform: translateY(50px); opacity: 0;}
    to {transform: translateY(0); opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# Session state
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

# Intro screen
if not st.session_state.unlocked:
    st.markdown('<div class="title">💖 Hey You 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">I made something special just for you...</div>', unsafe_allow_html=True)

    if st.button("✨ Click to Open Your Surprise ✨"):
        with st.spinner("Unlocking love... 💕"):
            time.sleep(2)
        st.session_state.unlocked = True
        st.rerun()

else:
    st.markdown('<div class="title">For My Love ❤️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Every moment with you is magic ✨</div>', unsafe_allow_html=True)

    # --- Frame 1 (Portrait) ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])  # center image
    with col2:
        st.image("img1.jpg", width=300)
    st.write("💫 *You walked into my life and made everything brighter.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Frame 2 (Landscape) ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("img2.jpg", use_container_width=True)
    st.write("🌸 *In a world full of chaos, you are my peace.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Frame 3 (Portrait) ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("img3.jpg", width=300)
    st.write("💖 *Every smile of yours is my favorite moment.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Frame 4 (Landscape) ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("img4.jpg", use_container_width=True)
    st.write("🌹 *I didn't believe in magic until I met you.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Frame 5 (Landscape) ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("img5.jpg", use_container_width=True)
    st.write("✨ *You are my today and all of my tomorrows.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # Final surprise
    st.markdown('<div class="title">💌 One Last Thing...</div>', unsafe_allow_html=True)

    if st.button("Click for a Surprise 💕"):
        st.balloons()
        st.success("I love you more than words can ever express ❤️")

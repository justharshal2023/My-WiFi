# 🌹 Love Site — Streamlit Deployment Guide

## Your project files
```
love_site/
├── app.py           ← Streamlit entry point
├── love.html        ← The beautiful website (copy from outputs)
├── requirements.txt ← Dependencies
└── README.md        ← This file
```

---

## 🚀 Deploy on Streamlit Community Cloud (Free)

### Step 1 — Push to GitHub
1. Create a **new private repository** on GitHub (private = only you can see it)
2. Upload these 3 files into it: `app.py`, `love.html`, `requirements.txt`

### Step 2 — Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
2. Click **"New app"**
3. Select your repository, branch (`main`), and set **Main file path** to `app.py`
4. Click **Deploy** — it'll be live in ~60 seconds! 🎉

### Step 3 — Share the link
You'll get a URL like `https://yourname-lovesite-app-xxxx.streamlit.app`
Send it to her with the password hint 💕

---

## 🔑 Changing the password
Open `love.html` in any text editor, find this line near the bottom:
```js
const PASSWORD = "iloveyou";
```
Change `"iloveyou"` to your own secret word.

---

## 📸 Adding her photos

### Why plain `<img src="photo.jpg">` doesn't work in Streamlit
Streamlit renders the HTML inside a sandboxed `<iframe>` — it has no access
to the local file system. **The updated `app.py` fixes this automatically**
by converting every local image to a Base64 data URL before rendering.

### Steps
1. Put your `.jpg` / `.png` files in the **same folder** as `app.py` & `love.html`
2. Open `love.html`, find the 5 photo placeholder sections:
   ```html
   <!-- 👉 Replace with: <img src="YOUR_IMAGE_1.jpg" alt=""/> -->
   📷
   ```
3. Replace the `📷` emoji with a proper img tag using the **exact filename**:
   ```html
   <img src="photo1.jpg" alt="" style="width:100%;height:100%;object-fit:cover;"/>
   ```
4. `app.py` will auto-read the file, base64-encode it, and inline it — works
   both locally and on Streamlit Cloud.

> **Tip:** Keep filenames simple — `photo1.jpg`, `photo2.jpg`, no spaces.

---

## 💻 Run locally (to preview before deploying)
```bash
pip install streamlit
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

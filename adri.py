# app.py

import streamlit as st
from datetime import date
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from base64 import b64encode
import base64
import os

# --- Background Image ---
# --- Background Image ---
st.set_page_config(page_title="A Journey of Us 💑", page_icon="💖", layout="wide")

# 
st.markdown("""
    <style>
    @keyframes floatUpDisappear {
        0% {
            bottom: -100px;
            opacity: 0;
            transform: translateX(-50%) scale(0.5);
        }
        10% {
            opacity: 1;
            transform: translateX(-50%) scale(1.2);
        }
        100% {
            bottom: 120%;
            opacity: 0;
            transform: translateX(-50%) scale(0.8);
        }
    }

    .floating-heart {
        position: fixed;
        bottom: -100px;
        left: 50%;
        font-size: 500px;
        color: #ff4d6d;
        z-index: 9999;
        pointer-events: none;
        animation: floatUpDisappear 5s ease-in-out forwards;
    }
    </style>

    <div class="floating-heart">❤️</div>
""", unsafe_allow_html=True)


def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- Page Config ---
set_background("1000206482.jpg")

# Page config



# Centered CSS + full layout control
st.markdown("""
    <style>
        body {
            text-align: center;
        }
        .centered-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
        }

        .stApp {
            text-align: center;
        }

        .stMarkdown, .stText, .stSubheader, .stTitle, .stCaption {
            text-align: center !important;
        }

        .stSlider > label, .stButton > button {
            margin-left: auto;
            margin-right: auto;
        }

        .stAudio, .stVideo {
            display: flex;
            justify-content: center;
        }

        /* Text color for dark background */
        .stApp, .stMarkdown, .stText, .stSubheader, .stTitle, .stCaption, p, div {
            color: #f0f0f0 !important;
        }

        a {
            color: #a8d0e6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💖 A Journey of Us 💑")
st.markdown("---")

# Love Letter
st.subheader("💌 A Love Letter")
st.markdown("""
<div class="centered-container">
<p>
Dear <strong>Adri 💖</strong>,<br><br>

From the moment our paths crossed, you've been the light of my life.<br>
Every day with you is a chapter in the most beautiful story I could ever imagine.<br>
This little app is a glimpse into our journey — the smiles, the memories, the love. 💕<br><br>

After our breakup, I finally understood what true love really means.<br>
The way you treated me — with patience, respect, and warmth — it was nothing short of <strong>a prince’s treatment</strong>.<br>
You showed me love that was pure, selfless, and strong. And through that, I realized the kind of woman you truly are — <strong>a real one</strong>. 🌹<br><br>

I still remember asking you once, “Who is your favorite hero?” and you smiled and said, <strong>“You.”</strong><br>
That moment lives in my heart forever. 💞<br><br>

The girl I fell for never looked at anyone else — for her, I was everything.<br>
Even when I misunderstood you or doubted you, your heart never changed.<br>
You always knew how to calm my anger, how to guide me when I lost my way.<br>
You weren’t just my love — you were, and still are, <strong>my queen 👑</strong>.<br><br>

On <strong>4th November</strong>, when I returned to you, I honestly didn’t expect you would accept me again.<br>
But you did — with the same open heart, with the same love that never faded.<br>
That day I realized something precious: <strong>you are rare, you are pure, and I never want to lose you again.</strong> 💫<br><br>

You are my peace after chaos, my calm after every storm, and the reason I believe in love again.<br><br>

With all my heart,<br>
<strong>Subha 💖</strong>
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Auto Image Slideshow
st.subheader("📸 Our Memories")

photo_files = [
    ("adri_in_bday.jpg", "Adri’s Birthday Celebration with me 🎂💖"),
    ("adri_in_bgarden.jpg", "Beautiful day in the Garden with me 🌸"),
    ("adri_in_khejurpukur.jpg", "Goofy selfies at Khejurpukur with me 😝"),
    ("adri_in_metcalfehall.jpg", "Special moments at Metcalfe Hall with me 🌈"),
    ("Adri_in_nandan.jpg", "Chilling at Nandan with me 🎬"),
    ("adri_in_srarswati_puja.jpg", "Saraswati Puja memories with me 🪷"),
    ("adri_in_zoo.jpg", "Fun at the zoo with me 🐯"),
    ("adri_mom_first_meet.jpg", "The day Adri’s mom met me for the first time ❤️")
]

encoded_images = []
captions = []

for img_path, caption in photo_files:
    try:
        with open(img_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_base64 = b64encode(img_bytes).decode("utf-8")
            encoded_images.append(f"data:image/jpeg;base64,{img_base64}")
            captions.append(caption)
    except FileNotFoundError:
        st.error(f"Image not found: {img_path}")

if encoded_images:

    # Convert Python lists to JS arrays as strings with quotes
    js_images = "[" + ",".join([f'"{img}"' for img in encoded_images]) + "]"
    js_captions = "[" + ",".join([f'"{cap}"' for cap in captions]) + "]"

    html_code = f"""
    <div style="display: flex; flex-direction: column; align-items: center;">
        <img id="slideshow" src={encoded_images[0]}
             style="max-width: 400px; width: 80%; height: auto; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);"/>
        <p id="caption" style="font-size: 17px; font-weight: bold; margin-top: 8px; color: #444; text-align: center;">
            {captions[0]}
        </p>
    </div>

    <script>
        const images = {js_images};
        const captions = {js_captions};
        let index = 0;
        setInterval(() => {{
            index = (index + 1) % images.length;
            document.getElementById("slideshow").src = images[index];
            document.getElementById("caption").textContent = captions[index];
        }}, 3000);
    </script>
    """

    components.html(html_code, height=600)


# Map of Places


st.subheader("🗺️ Places We've Been Together 💞")

# Center point (Kolkata)
st.image("Screenshot (72).png", caption="Places we have spent romantic time together 🎂💖", use_container_width=True)

st.markdown("---")
st.subheader("👩‍👩‍👧 Adri’s Beautiful Family 💕")

family_photos = [
    ("Adri_with_family.jpg", "Adri with her lovely family 💖"),
    ("adri_with_didi.jpg", "Smiles that light up the day with her elder sister🌟"),
]

for img_path, caption in family_photos:
    try:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{base64.b64encode(open(img_path, "rb").read()).decode()}" 
                         style="max-width: 400px; width: 90%; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);"/>
                    <p style="margin-top: 8px; font-weight: bold; color: #f0f0f0;">{caption}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"Family image not found: {img_path}")
st.markdown("---")
# Timeline
st.subheader("🗓️ Our Love Timeline")
timeline = {
    "2024-05-06": "💍 The Day I Proposed — and my heart found its home 💖",
    "2025-01-07": "🌳 Our last walk in Khejurpukur Park — calm and special 🌅",
    "2025-01-16": "🦁 Fun day at Alipore Zoo — laughter, love, and silly faces 🐾",
    "2025-01-21": "🌸 Botanical Garden Visit — peaceful moments hand in hand 🌿",
    "2025-01-28": "👩‍👩‍👧 First time meeting her mom — nerves, smiles & warmth 💞",
    "2025-01-28B": "🏛️ Metcalfe Hall Visit — captured memories forever 📸",
    "2025-02-03": "🪷 Saraswati Puja — she looked like a goddess that day 💫",
    "2025-02-10": "🎂 Adri’s Birthday Celebration — smiles, cake & love ❤️",
    "2025-02-13": "💔 The 11:55 pm Breakup — tears and lessons 💭",
    "2025-11-04": "💞 The Return — I came back to her, and she gave me one last beautiful chance 🌈",
}

for d, event in sorted(timeline.items()):
    st.markdown(f"**{d}** — {event}")

st.markdown("---")

# Playlist
st.subheader("🎶 Our Songs")
st.markdown("""
- **Perfect** — Ed Sheeran  
- **Can't Help Falling in Love** — Elvis Presley  
- **All of Me** — John Legend  
""")
st.audio("Feel The Talwiinder Mashup 2024  Khayaal X Gallan 4 X Dhundhala X Nasha X Tu  Sunny Hassan.mp3", format="audio/mp3")
st.markdown("---")

# Video
st.subheader("🎥 A Video Just for You")
st.markdown("Here's something special I made with all my heart...")

with st.expander("🎥 Watch Our Special Video"):
    video_path = "WhatsApp Video 2025-11-05 at 9.59.03 PM.mp4"
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning("Video file not found!")

# Surprise
st.subheader("🎁 A Special Surprise")
if st.button("Click to Reveal"):
    st.balloons()
    st.success("You are the best part of my every day. ❤️ I love you.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ love by [Subha  ❤️]")

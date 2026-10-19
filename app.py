import streamlit as st
import base64

# Page ka title aur layout set karein
st.set_page_config(page_title="Happy Birthday! 🎉", page_icon="🎂", layout="centered")

# Automatic balloons udane ke liye
st.balloons()

# App ka main heading aur message
st.title("🎉 Happy Birthday to You! 🎂")
st.write("""
Dua hai ki aapki zindagi ka har lamha khushiyon se bhara ho, 
aur aapko wo sab mile jo aap chahte hain! Stay blessed hamesha! ❤️
""")

# Background me automatic audio play karne ka function
def play_bg_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # HTML audio tag jisme autoplay aur loop dono lagaya hai
            audio_html = f"""
                <audio autoplay="true" loop="true" style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(audio_html, unsafe_allow_html=True)
            st.success("🎶 Background music chalu ho gaya hai! Enjoy! 🥳")
    except FileNotFoundError:
        st.error("⚠️ Error: GitHub par song file nahi mili!")

# Aapke song ka naam yahan automatic play ke liye daal diya hai
play_bg_audio("nastelbom-happy-birthday-49526.mp3")

# Sunder look dene ke liye ek birthday image
st.markdown("---")
st.image("https://unsplash.com", caption="Have a Blast! 🎁")

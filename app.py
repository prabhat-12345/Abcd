import streamlit as st

# Page ka title aur layout set karein
st.set_page_config(page_title="Happy Birthday! 🎉", page_icon="🎂", layout="centered")

# App ka main heading
st.title("🎉 Happy Birthday to You! 🎂")
st.subheader("Aapke liye ek special surprise hai... 👇")

# Ek pyaara sa birthday message
st.write("""
Dua hai ki aapki zindagi ka har lamha khushiyon se bhara ho, 
aur aapko wo sab mile jo aap chahte hain! Stay blessed hamesha! ❤️
""")

# Jab user is button par click karega toh balloons urenge aur gaana bajega
if st.button("🎈 Surprise Dekho Aur Song Suno! 🎈", use_container_width=True):
    # 1. Screen par balloons udane ke liye
    st.balloons()
    
    # 2. Gaana play karne ke liye (Aapki file ka exact naam yahan daal diya hai)
    try:
        audio_file = open("nastelbom-happy-birthday-49526.mp3", "rb")
        audio_bytes = audio_file.read()
        
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        st.success("🎶 Baar baar din ye aaye... Gaana baj raha hai! Enjoy! 🥳")
        
    except FileNotFoundError:
        st.error("⚠️ Error: Code me naam sahi hai, par check karo GitHub pe spelling yahi hai na?")

# Card jaisa look dene ke liye ek chota sa container
with st.container():
    st.markdown("---")
    st.image("https://unsplash.com", caption="Have a Blast! 🎁")
    

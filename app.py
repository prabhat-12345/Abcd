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
    
    # 2. Gaana play karne ke liye (File ka naam 'birthday.mp3' rakha hai)
    try:
        audio_file = open("birthday.mp3", "rb")
        audio_bytes = audio_file.read()
        
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        st.success("🎶 Baar baar din ye aaye... Gaana baj raha hai! Enjoy! 🥳")
        
    except FileNotFoundError:
        st.error("⚠️ Error: 'birthday.mp3' file nahi mili! Phele GitHub pe 'birthday.mp3' naam se song upload karo bhaiya!")

# Card jaisa look dene ke liye ek chota sa container
with st.container():
    st.markdown("---")
    st.image("https://unsplash.com", caption="Have a Blast! 🎁")
  

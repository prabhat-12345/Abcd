import streamlit as st
import base64

# 1. Custom High-End Page Setup
st.set_page_config(
    page_title="Happy Birthday Anshika | 2 Years of Memories", 
    page_icon="👑", 
    layout="centered"
)

# 2. Advanced Multi-Color Light Changing Background & Royal Neon Fonts (CSS Injector)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* 🌈 Smooth dynamic color shifting background */
    @keyframes romanticGlowBackground {
        0% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
        33% { background: linear-gradient(135deg, #150321 0%, #29051d 100%); }
        66% { background: linear-gradient(135deg, #040d1a 0%, #110321 100%); }
        100% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
    }
    
    /* ⚡ Neon light border animations for photo frame */
    @keyframes neonBorderGlow {
        0% { border-color: #ec4899; box-shadow: 0 0 20px rgba(236, 72, 153, 0.6); }
        50% { border-color: #38bdf8; box-shadow: 0 0 20px rgba(56, 189, 248, 0.7); }
        100% { border-color: #fbbf24; box-shadow: 0 0 20px rgba(251, 191, 36, 0.6); }
    }

    .stApp {
        animation: romanticGlowBackground 12s ease-in-out infinite;
        color: #ffffff !important;
        background-size: 400% 400%;
        overflow-y: auto !important;
    }
    
    /* Elegant Frame for Permanent Photo */
    .photo-frame {
        border: 4px solid #ec4899;
        border-radius: 25px;
        padding: 10px;
        background: rgba(15, 6, 26, 0.6);
        animation: neonBorderGlow 6s linear infinite;
        margin-top: 20px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .cyber-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.1rem;
        color: #38bdf8 !important;
        text-shadow: 0 0 12px rgba(56, 189, 248, 0.7);
        text-align: center;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    
    .gold-accent {
        color: #fbbf24 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 1.05rem;
        text-shadow: 0 0 8px rgba(251, 191, 36, 0.4);
        text-align: center;
    }
    
    /* Dream Cursive Quotes Style (Without Writer Name) */
    .premium-quote {
        font-family: 'Alex Brush', cursive;
        color: #ffd700 !important;
        font-size: 2.8rem;
        line-height: 1.4;
        margin: 30px 0 25px 0;
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.6);
        text-align: center;
    }
    
    /* 💎 ULTRA-PREMIUM DYNAMIC NEON GLOW FOR HAPPY BIRTHDAY ANSHIKA */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        color: #ffffff !important;
        /* Double neon glow layer (Pink + Cyan Blue) */
        text-shadow: 0 0 10px #fff, 0 0 20px #ec4899, 0 0 30px #ec4899, 0 0 40px #38bdf8, 0 0 70px #38bdf8;
        margin-top: 45px;
        margin-bottom: 35px;
        letter-spacing: 5px;
        text-align: center;
        animation: neonPulse 2s ease-in-out infinite alternate;
    }

    @keyframes neonPulse {
        from { text-shadow: 0 0 10px #fff, 0 0 20px #ec4899, 0 0 30px #ec4899, 0 0 40px #38bdf8; }
        to { text-shadow: 0 0 15px #fff, 0 0 30px #ff73b9, 0 0 45px #ff73b9, 0 0 60px #70d5ff; }
    }

    /* Target Streamlit's custom primary buttons for premium branding */
    .stButton>button {
        background: linear-gradient(90deg, #ec4899, #38bdf8) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(56, 189, 248, 0.6) !important;
    }

    /* Hide standard top header bars */
    .stDeployButton, footer, header {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Premium Live FX Modules
st.balloons()
st.snow()

# 4. Main Header Interface
st.markdown('<div style="text-align: center; font-size: 2rem; margin-bottom: 5px;">✨ 👑 ✨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="cyber-title">A CELEBRATION OF EXCELLENCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="gold-accent">🌹 Beyond Guiding, A Special Bond of Lifetime 🌹</p>', unsafe_allow_html=True)

# 5. 100% WORKING AUDIO BUTTON ENGINE
if st.button("🎵 Click Here to Play Birthday Song 🎵", use_container_width=True):
    try:
        with open("nastelbom-happy-birthday-49526.mp3", "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    except FileNotFoundError:
        st.error("⚠️ File Read Error: Check if audio file name matches on GitHub.")

# 📸 PHOTO DISPLAY FRAME BLOCK
st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
try:
    with open("anshika.jpg", "rb") as img_file:
        img_bytes = img_file.read()
    st.image(img_bytes, use_container_width=True)
except FileNotFoundError:
    st.markdown('<div style="font-size: 4.5rem; padding: 10px 0;">💖</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Dream Focused Quotes Curation (Without Writer Names) ---
st.markdown('<p class="premium-quote">"May your dreams be larger than mountains, and may your courage to chase them always match the brilliance of your mind."</p>', unsafe_allow_html=True)

st.markdown('<p class="premium-quote">"The magic happens when a brilliant intellect dares to dream. Keep shining, because the stars are waiting for you."</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(56, 189, 248, 0.4); margin: 35px 0;">', unsafe_allow_html=True)

# --- 2 Years Journey & Emotional/Romantic Narrative Block ---
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.9; text-align: center; color: #ffffff; padding: 0 10px;">
    Teaching you for the last <span style="color: #fbbf24; font-weight: 700;">2 beautiful years</span> has been the most profound privilege of my life. 
    What started as a journey of mentor and student slowly grew into a <span style="color: #38bdf8; font-weight: 700;">beautiful, unforgettable friendship</span> 
    that I cherish more than words can say. 
    <br><br>
    Every conversation, every shared goal, and every milestone we crossed together has made these two years completely <span style="color: #ec4899; font-weight: 700;">memorable and irreplaceable</span>. 
    Somewhere between guiding your brilliant intellect and listening to your dreams, my heart quietly fell for the wonderful soul you are. 
    You became the rhythm to my silence and the secret sparkle in my ordinary days. 
    <br><br>
    Your potential is absolutely limitless, and no matter how far your dreams take you, remember that you have someone who always believes in you, cares for you, and secretly holds you close in every thought.
</div>
""", unsafe_allow_html=True)

# 🚀 PREMIUM HIGH-INTENSITY DYNAMIC NEON TEXT AT THE ABSOLUTE BOTTOM
st.markdown('<div class="slow-reveal">H A P P Y &nbsp; B I R T H D A Y &nbsp; A N S H I K A</div>', unsafe_allow_html=True)

# Footer Layout
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #a855f7; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 20px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

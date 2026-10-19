import streamlit as st
import base64

# 1. Custom High-End Page Setup
st.set_page_config(
    page_title="H A P P Y  B I R T H D A Y  A N S H I K A", 
    page_icon="👑", 
    layout="centered"
)

# 2. Smooth RGB Light Changing Background & Premium Fonts (CSS Injector)
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
    
    /* ⚡ Neon light border animations */
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
    
    /* Luxury Card Framework with Auto-Height visibility */
    .luxury-card {
        background: rgba(12, 5, 22, 0.88);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 3px solid #ec4899;
        border-radius: 25px;
        padding: 35px 25px;
        animation: neonBorderGlow 6s linear infinite;
        margin-top: 15px;
        margin-bottom: 30px;
        text-align: center;
        height: auto !important; /* Fixes text hiding at the bottom */
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
    }
    
    .premium-quote {
        font-family: 'Alex Brush', cursive;
        color: #ffd700 !important;
        font-size: 2.5rem;
        line-height: 1.3;
        margin: 20px 0 5px 0;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    .author-tag {
        color: #38bdf8 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-bottom: 25px;
    }
    
    /* 🚀 Fix: Clear visibility for the birthday text */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 1.9rem;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(236, 72, 153, 0.9), 0 0 40px rgba(168, 85, 247, 0.6);
        margin-top: 35px;
        margin-bottom: 15px;
        letter-spacing: 3px;
        display: block !important;
        text-align: center;
    }
    
    /* Elegant Frame for Permanent Photo */
    .photo-frame {
        border: 3px solid rgba(255, 215, 0, 0.6);
        border-radius: 20px;
        padding: 5px;
        background: linear-gradient(45deg, #ec4899, #fbbf24);
        box-shadow: 0 0 20px rgba(236, 72, 153, 0.4);
        margin-bottom: 25px;
    }
    
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
st.markdown('<p class="gold-accent">🌹 Dedicated to an exceptional mind on her special day 🌹</p>', unsafe_allow_html=True)

# 5. Main Glowing Luxury Card Layout Container
st.markdown('<div class="luxury-card">', unsafe_allow_html=True)

# 📸 PERMANENT PHOTO CODE BLOCK
try:
    # GitHub repository se seedhe photo load karega
    with open("anshika.jpg", "rb") as img_file:
        img_bytes = img_file.read()
    st.image(img_bytes, use_container_width=True)
except FileNotFoundError:
    # Agar abhi tak upload nahi kiya hai toh ye default premium crown placeholder dikhega
    st.markdown('<div style="font-size: 4.5rem; padding: 10px 0; filter: drop-shadow(0 0 12px #ec4899);">👑</div>', unsafe_allow_html=True)
    st.info("💡 Tip: Apni repo me 'anshika.jpg' naam se photo upload kar do, wo yahan automatic lag jayegi!")

# --- Premium Quotes Matrix ---
st.markdown('<p class="premium-quote">"The future belongs to those who believe in the beauty of their dreams."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Eleanor Roosevelt</p>', unsafe_allow_html=True)

st.markdown('<p class="premium-quote">"In a world where you can be anything, be the intellect that inspires and the grace that lights up the room."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Luxury Curation</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(56, 189, 248, 0.4); margin: 20px 0;">', unsafe_allow_html=True)

# Deep Appreciation Message
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; text-align: center; color: #ffffff; font-weight: 600; margin-bottom: 25px;">
It is a profound privilege to guide a student with your <span style="color: #fbbf24; font-weight: 800;">brilliant intellect</span>, 
relentless dedication, and unwavering curiosity. Your potential is absolutely limitless!
</div>
""", unsafe_allow_html=True)

# --- Safe High-Fidelity Audio Player Inside Card ---
try:
    with open("nastelbom-happy-birthday-49526.mp3", "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
except FileNotFoundError:
    st.markdown("<p style='color:#f87171;'>⚠️ Audio track connection issue.</p>", unsafe_allow_html=True)

# 🚀 CRITICAL VISIBILITY FIX: Text spacing aur placement fix kar diya hai!
st.markdown('<div class="slow-reveal">H A P P Y &nbsp; B I R T H D A Y &nbsp; A N S H I K A</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer Layout
st.markdown(
    '<div style="text-align: center; color: #a855f7; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 20px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

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
    
    /* 🌈 Dhire-dhire dynamic rang badalne wala background animation */
    @keyframes romanticGlowBackground {
        0% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
        33% { background: linear-gradient(135deg, #150321 0%, #29051d 100%); }
        66% { background: linear-gradient(135deg, #040d1a 0%, #110321 100%); }
        100% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
    }
    
    /* ⚡ Luxury glowing borders for the card */
    @keyframes neonBorderGlow {
        0% { border-color: #ec4899; box-shadow: 0 0 20px rgba(236, 72, 153, 0.5); }
        50% { border-color: #38bdf8; box-shadow: 0 0 20px rgba(56, 189, 248, 0.6); }
        100% { border-color: #fbbf24; box-shadow: 0 0 20px rgba(251, 191, 36, 0.5); }
    }

    .stApp {
        animation: romanticGlowBackground 12s ease-in-out infinite;
        color: #ffffff !important;
        background-size: 400% 400%;
        overflow-y: auto !important; /* Force enable standard scrolling */
    }
    
    /* Glassmorphism Transparent Card Template */
    .luxury-card {
        background: rgba(15, 6, 26, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 3px solid #ec4899;
        border-radius: 25px;
        padding: 35px 25px;
        animation: neonBorderGlow 6s linear infinite;
        margin-top: 15px;
        text-align: center;
    }
    
    /* Clear Visible Typography elements */
    .cyber-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        color: #38bdf8 !important;
        text-shadow: 0 0 12px rgba(56, 189, 248, 0.7);
        text-align: center;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }
    
    .gold-accent {
        color: #fbbf24 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        text-align: center;
        font-size: 1.05rem;
    }
    
    .premium-quote {
        font-family: 'Alex Brush', cursive;
        color: #ffd700 !important;
        font-size: 2.6rem;
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
        margin-bottom: 20px;
    }
    
    /* Smooth fading text block at the absolute bottom */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 1.7rem;
        color: #ffffff !important;
        text-shadow: 0 0 15px rgba(236, 72, 153, 0.8), 0 0 30px rgba(168, 85, 247, 0.5);
        margin-top: 30px;
        letter-spacing: 3px;
        opacity: 0;
        transform: translateY(20px);
        animation: smoothSlideUp 3s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    }
    
    @keyframes smoothSlideUp {
        0% { opacity: 0; transform: translateY(30px); filter: blur(4px); }
        100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    
    /* Clean layout control overrides */
    .stDeployButton, footer, header {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. FX Modules (Automatic Balloons & Snowfall on Start)
st.balloons()
st.snow()

# 4. Main Title Interface Block
st.markdown('<div style="text-align: center; font-size: 2rem; margin-bottom: 5px;">✨ 👑 ✨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="cyber-title">A CELEBRATION OF EXCELLENCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="gold-accent">🌹 Dedicated to an exceptional mind on her special day 🌹</p>', unsafe_allow_html=True)

# Sidebar setup for live uploads
st.sidebar.markdown("### 🖼️ Studio Media Center")
uploaded_image = st.sidebar.file_uploader("Upload Anshika's Photo Here", type=["jpg", "png", "jpeg", "webp"])

# 5. Main Glowing Luxury Card Layout Container
st.markdown('<div class="luxury-card">', unsafe_allow_html=True)

# Image placement layout
if uploaded_image is not None:
    st.image(uploaded_image, use_container_width=True)
else:
    st.markdown('<div style="font-size: 4.5rem; padding: 10px 0; filter: drop-shadow(0 0 12px #ec4899);">💖</div>', unsafe_allow_html=True)

# Premium Beautiful Quotes Segment
st.markdown('<p class="premium-quote">"The future belongs to those who believe in the beauty of their dreams."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Eleanor Roosevelt</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(56, 189, 248, 0.3); margin: 15px 0;">', unsafe_allow_html=True)

# Dynamic Heartfelt Appreciation Message block
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; line-height: 1.7; text-align: center; color: #ffffff; font-weight: 600; margin-bottom: 25px;">
It is a profound privilege to guide a student with your <span style="color: #fbbf24; font-weight: 800;">brilliant intellect</span>, 
relentless dedication, and unwavering curiosity. Your potential is absolutely limitless!
</div>
""", unsafe_allow_html=True)

# Safe High-Fidelity Audio player integrated directly inside the card framework
try:
    with open("nastelbom-happy-birthday-49526.mp3", "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
except FileNotFoundError:
    st.markdown("<p style='color:#f87171;'>⚠️ Audio track connection issue. Check file on repo.</p>", unsafe_allow_html=True)

# Happy Birthday Anshika - Smooth sliding text block at the absolute bottom
st.markdown('<div class="slow-reveal">H A P P Y &nbsp; B I R T H D A Y &nbsp; A N S H I K A</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Aesthetic Footer Layer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #a855f7; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

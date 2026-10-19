import streamlit as st
import base64

# 1. Custom High-End Page Setup
st.set_page_config(
    page_title="H A P P Y  B I R T H D A Y  A N S H I K A", 
    page_icon="👑", 
    layout="centered"
)

# 2. Advanced Multi-Color Light Changing Theme & Elegant Typography (CSS Injector)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* 🌈 Background color shifting smoothly */
    @keyframes romanticGlowBackground {
        0% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
        33% { background: linear-gradient(135deg, #150321 0%, #29051d 100%); }
        66% { background: linear-gradient(135deg, #040d1a 0%, #110321 100%); }
        100% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
    }
    
    /* ⚡ Border neon pulses */
    @keyframes neonBorderGlow {
        0% { border-color: #ec4899; box-shadow: 0 0 25px rgba(236, 72, 153, 0.6); }
        50% { border-color: #38bdf8; box-shadow: 0 0 25px rgba(56, 189, 248, 0.7); }
        100% { border-color: #fbbf24; box-shadow: 0 0 25px rgba(251, 191, 36, 0.6); }
    }

    .stApp {
        animation: romanticGlowBackground 10s ease-in-out infinite;
        color: #ffffff !important;
        background-size: 400% 400%;
    }
    
    /* Luxury Transparent Neon Card */
    .luxury-card {
        background: rgba(10, 4, 18, 0.85);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 3px solid #ec4899;
        border-radius: 25px;
        padding: 40px 30px;
        animation: neonBorderGlow 6s linear infinite;
        margin-top: 20px;
        text-align: center;
    }
    
    /* 💎 CRYSTAL CLEAR NEON TEXT COLORS FOR HIGH VISIBILITY */
    .cyber-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.3rem;
        color: #38bdf8 !important; /* Vibrant Cyan Blue */
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.8);
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 15px;
        line-height: 1.4;
    }
    
    .gold-accent {
        color: #fbbf24 !important; /* Pure Bright Gold */
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
        text-align: center;
        font-size: 1.1rem;
        text-shadow: 0 0 8px rgba(251, 191, 36, 0.4);
    }
    
    /* ✨ Beautiful Cursive Style for Quotes */
    .premium-quote {
        font-family: 'Alex Brush', cursive;
        color: #ffd700 !important; /* Bright Yellow Gold */
        font-size: 2.8rem;
        line-height: 1.3;
        margin: 25px 0 10px 0;
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.6);
        text-align: center;
    }
    
    .author-tag {
        color: #38bdf8 !important; 
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 3px;
        font-size: 1rem;
        text-transform: uppercase;
        margin-bottom: 25px;
    }
    
    /* Slow Fade & Reveal Effect for Spaced Bottom Title */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 1.8rem;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(236, 72, 153, 0.9), 0 0 40px rgba(168, 85, 247, 0.7);
        margin-top: 35px;
        letter-spacing: 4px;
        opacity: 0;
        transform: translateY(20px);
        animation: smoothSlideUp 3.5s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    }
    
    @keyframes smoothSlideUp {
        0% { opacity: 0; transform: translateY(40px); filter: blur(5px); }
        100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    
    /* Clean UI Overrides */
    .stDeployButton, footer, header {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Smart Autoplay Global Audio Engine (Fixed to use your exact file name)
def play_system_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_html = f"""
                <div id="click-overlay" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:99999; cursor:pointer; display:block;" onclick="document.getElementById('bg-audio').play(); this.style.display='none';">
                    <p style="color:rgba(255,255,255,0.4); text-align:center; margin-top:10px; font-size:12px; font-family:sans-serif; background:rgba(0,0,0,0.5); padding:5px;">✨ Tap anywhere on screen to unmute the music experience ✨</p>
                </div>
                <audio id="bg-audio" loop style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    document.addEventListener('DOMContentLoaded', function() {{
                        var audio = document.getElementById('bg-audio');
                        audio.play().catch(function(error) {{
                            console.log("Interaction required.");
                        }});
                    }});
                </script>
                """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.sidebar.error("⚠️ File read error. Ensure name matches exactly on repository.")

# 🚨 AAPKI SCREENSHOT WALI GAANE KI FILE KA EXACT NAAM HAIN YAHAN
play_system_audio("nastelbom-happy-birthday-49526.mp3")

# 4. Premium Live Animations
st.balloons()
st.snow()

# 5. UI Render Matrix
st.markdown('<div style="text-align: center; font-size: 2.2rem; margin-bottom: 5px;">✨ 👑 ✨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="cyber-title">A CELEBRATION OF EXCELLENCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="gold-accent">🌹 Dedicated to an exceptional mind on her special day 🌹</p>', unsafe_allow_html=True)

# Sidebar setup for live uploads
st.sidebar.markdown("### 🖼️ Studio Media Center")
uploaded_image = st.sidebar.file_uploader("Upload Anshika's Photo Here", type=["jpg", "png", "jpeg", "webp"])

# Main Glowing Luxury Card Layout
st.markdown('<div class="luxury-card">', unsafe_allow_html=True)

if uploaded_image is not None:
    st.image(uploaded_image, use_container_width=True)
else:
    # Golden Luxury Heart Placeholder
    st.markdown('<div style="font-size: 5rem; padding: 15px 0; filter: drop-shadow(0 0 15px #ec4899);">💖</div>', unsafe_allow_html=True)

# English Premium Quotes
st.markdown('<p class="premium-quote">"The future belongs to those who believe in the beauty of their dreams."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Eleanor Roosevelt</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(56, 189, 248, 0.4); ">', unsafe_allow_html=True)

# Deep Heartfelt Text Message
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; text-align: center; color: #ffffff; font-weight:600;">
It is a profound privilege to guide a student with your <span style="color: #fbbf24; font-weight: 800;">brilliant intellect</span>, 
relentless dedication, and unwavering curiosity. Your potential is absolutely limitless!
</div>
""", unsafe_allow_html=True)

# 🚀 EK-EK WORD ME SPACE KE SAATH DHIRE-DHIRE AANE WALA ANIMATED TEXT
st.markdown('<div class="slow-reveal">H A P P Y &nbsp; B I R T H D A Y &nbsp; A N S H I K A</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer Layout
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #a855f7; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

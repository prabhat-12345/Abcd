import streamlit as st
import base64

# 1. Custom High-End Page Setup
st.set_page_config(
    page_title="H A P P Y  B I R T H D A Y  A N S H I K A", 
    page_icon="👑", 
    layout="centered"
)

# 2. Advanced Multi-Color Light Changing Background & Ultra Visible Fonts (CSS Injector)
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
        overflow-y: auto !important; /* Force standard scrolling completely free */
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
    
    /* Dynamic Quotes Layout */
    .premium-quote {
        font-family: 'Alex Brush', cursive;
        color: #ffd700 !important;
        font-size: 2.7rem;
        line-height: 1.3;
        margin: 25px 0 5px 0;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
        text-align: center;
    }
    
    .author-tag {
        color: #38bdf8 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Bright neon text at the absolute bottom */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2rem;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(236, 72, 153, 0.9), 0 0 40px rgba(168, 85, 247, 0.7);
        margin-top: 40px;
        margin-bottom: 30px;
        letter-spacing: 4px;
        text-align: center;
    }

    /* Target Streamlit's internal audio player wrapper to remove dark blocks */
    div[data-testid="stAudio"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Hide default elements cleanly */
    .stDeployButton, footer, header {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Clean Autoplay Execution Context (Fixes Screen Freeze)
def play_system_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Injected native standard audio player completely hidden
            audio_html = f"""
                <audio autoplay="true" loop="true" style="display:none;" id="bg-audio-engine">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    window.addEventListener('click', function() {{
                        var audio = document.getElementById('bg-audio-engine');
                        if (audio) {{
                            audio.play();
                        }}
                    }}, {{ once: true }});
                    window.addEventListener('touchstart', function() {{
                        var audio = document.getElementById('bg-audio-engine');
                        if (audio) {{
                            audio.play();
                        }}
                    }}, {{ once: true }});
                </script>
                """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Executing using your exact repository sound file
play_system_audio("nastelbom-happy-birthday-49526.mp3")

# 4. Premium Live FX Modules
st.balloons()
st.snow()

# 5. Main Header Interface
st.markdown('<div style="text-align: center; font-size: 2rem; margin-bottom: 5px;">✨ 👑 ✨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="cyber-title">A CELEBRATION OF EXCELLENCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="gold-accent">🌹 Dedicated to an exceptional mind on her special day 🌹</p>', unsafe_allow_html=True)

# 📸 PHOTO DISPLAY FRAME BLOCK
st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
try:
    with open("anshika.jpg", "rb") as img_file:
        img_bytes = img_file.read()
    st.image(img_bytes, use_container_width=True)
except FileNotFoundError:
    st.markdown('<div style="font-size: 4.5rem; padding: 10px 0;">💖</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Premium Quotes Matrix ---
st.markdown('<p class="premium-quote">"The future belongs to those who believe in the beauty of their dreams."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Eleanor Roosevelt</p>', unsafe_allow_html=True)

st.markdown('<p class="premium-quote">"In a world where you can be anything, be the intellect that inspires and the grace that lights up the room."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Luxury Curation</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(56, 189, 248, 0.4); margin: 30px 0;">', unsafe_allow_html=True)

# Heartfelt Text Message Block
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.15rem; line-height: 1.8; text-align: center; color: #ffffff; font-weight: 600; margin: 20px 0;">
It is a profound privilege to guide a student with your <span style="color: #fbbf24; font-weight: 800;">brilliant intellect</span>, 
relentless dedication, and unwavering curiosity. Your potential is absolutely limitless!
</div>
""", unsafe_allow_html=True)

# 🚀 Bright neon animated text at the absolute bottom
st.markdown('<div class="slow-reveal">H A P P Y &nbsp; B I R T H D A Y &nbsp; A N S H I K A</div>', unsafe_allow_html=True)

# Footer Layout
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #a855f7; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 20px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

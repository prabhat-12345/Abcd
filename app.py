import streamlit as st
import base64

# 1. Custom High-End Page Setup
st.set_page_config(
    page_title="For My Brightest Student | Anshika", 
    page_icon="👑", 
    layout="centered"
)

# 2. Advanced Multi-Color Light Changing Theme & Elegant Typography (CSS Injector)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* 🌈 Dhire-dhire dynamic light change karne wala background */
    @keyframes romanticGlowBackground {
        0% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
        33% { background: linear-gradient(135deg, #150321 0%, #29051d 100%); }
        66% { background: linear-gradient(135deg, #040d1a 0%, #110321 100%); }
        100% { background: linear-gradient(135deg, #090214 0%, #170529 100%); }
    }
    
    /* ⚡ Border ka neon light badalne ke liye animation */
    @keyframes neonBorderGlow {
        0% { border-color: #a855f7; box-shadow: 0 0 25px rgba(168, 85, 247, 0.4); }
        50% { border-color: #ec4899; box-shadow: 0 0 25px rgba(236, 72, 153, 0.5); }
        100% { border-color: #38bdf8; box-shadow: 0 0 25px rgba(56, 189, 248, 0.4); }
    }

    .stApp {
        animation: romanticGlowBackground 12s ease-in-out infinite;
        color: #ffffff !important;
        background-size: 400% 400%;
    }
    
    /* Luxury Transparent Neon Card */
    .luxury-card {
        background: rgba(15, 6, 26, 0.75);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid #a855f7;
        border-radius: 25px;
        padding: 40px 30px;
        animation: neonBorderGlow 8s linear infinite;
        margin-top: 20px;
        text-align: center;
    }
    
    /* Cyber/Neon Main Header */
    .cyber-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.8rem;
        background: linear-gradient(90deg, #ec4899, #fbbf24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -0.5px;
        margin-bottom: 5px;
    }
    
    .gold-accent {
        color: #fbbf24 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        text-align: center;
        font-size: 1rem;
    }
    
    /* ✨ Ultra Elegant Handwritten Cursive Style for Quotes */
    .premium-quote {
        font-family: 'Alex Brush', cursive;
        color: #ffd700 !important; /* Royal Matte Gold */
        font-size: 2.5rem;
        line-height: 1.3;
        margin: 20px 0 10px 0;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
        text-align: center;
    }
    
    .author-tag {
        color: #38bdf8 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 3px;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-bottom: 25px;
    }
    
    /* Slow Fade & Reveal Effect for Happy Birthday Anshika */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.3rem;
        color: #ffffff;
        text-shadow: 0 0 20px rgba(236, 72, 153, 0.9), 0 0 40px rgba(168, 85, 247, 0.6);
        margin-top: 30px;
        opacity: 0;
        transform: translateY(20px);
        animation: smoothSlideUp 4s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    }
    
    @keyframes smoothSlideUp {
        0% { opacity: 0; transform: translateY(40px); filter: blur(8px); }
        50% { opacity: 0.4; }
        100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    
    /* Clean UI Overrides */
    .stDeployButton, footer, header {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Smart Autoplay Global Audio Engine (Fixes browser mute block)
def play_system_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # HTML code jo pure browser window par touch intercept karke music chalu kar dega
            audio_html = f"""
                <div id="click-overlay" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:99999; cursor:pointer; display:block;" onclick="document.getElementById('bg-audio').play(); this.style.display='none';">
                    <p style="color:rgba(255,255,255,0.1); text-align:center; margin-top:2px; font-size:10px;">🎶 Tap anywhere to enable sound experience</p>
                </div>
                <audio id="bg-audio" loop style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    // Try auto playing immediately
                    document.addEventListener('DOMContentLoaded', function() {{
                        var audio = document.getElementById('bg-audio');
                        audio.play().catch(function(error) {{
                            console.log("Autoplay blocked. Waiting for user interaction overlay.");
                        }});
                    }});
                </script>
                """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.sidebar.error("⚠️ GitHub par 'happy.mp3' file nahi mili! Name sahi check karein.")

# 🚨 APNE SONG KA NAAM GITHUB PAR 'happy.mp3' RAKHEIN
play_system_audio("happy.mp3")

# 4. Premium Live Animations
st.balloons()
st.snow()

# 5. UI Render Matrix
st.markdown('<div style="text-align: center; font-size: 2.2rem; margin-bottom: 5px;">✨ 👑 ✨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="cyber-title">A Celebration of Excellence</h1>', unsafe_allow_html=True)
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

# Elegant Handwriting Cursive Script Font Quotes
st.markdown('<p class="premium-quote">"The future belongs to those who believe in the beauty of their dreams."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— Eleanor Roosevelt</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(236, 72, 153, 0.25); ">', unsafe_allow_html=True)

# Deep Heartfelt Text Message
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; line-height: 1.8; text-align: center; color: #e5def0;">
It is a profound privilege to guide a student with your <span style="color: #38bdf8; font-weight: 600;">brilliant intellect</span>, 
relentless dedication, and unwavering curiosity. Your potential is absolutely limitless!
</div>
""", unsafe_allow_html=True)

# Slow Slide and Reveal Animation Text at bottom
st.markdown('<div class="slow-reveal">✨ Happy Birthday Anshika 🎂 ✨</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer Layout
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #58446c; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 600; letter-spacing: 2px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

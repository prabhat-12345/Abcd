import streamlit as st
import base64

# 1. High-End Custom Page Configuration
st.set_page_config(
    page_title="A Celebration of Excellence | Anshika", 
    page_icon="✨", 
    layout="centered"
)

# 2. Pure Premium Dark Mode & Animation Matrix (CSS Injector)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* Royal Dark Gradient Background */
    .stApp {
        background: linear-gradient(185deg, #0b031a 0%, #17072b 50%, #05010d 100%) !important;
        color: #ffffff !important;
    }
    
    /* Neon Glowing Premium Card */
    .luxury-card {
        background: rgba(25, 12, 43, 0.65);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 2px solid #a855f7;
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 0 30px rgba(168, 85, 247, 0.25), inset 0 0 15px rgba(236, 72, 153, 0.1);
        margin-top: 25px;
        text-align: center;
    }
    
    /* Cyber Title Styling */
    .cyber-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 3rem;
        background: linear-gradient(90deg, #38bdf8, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 5px;
    }
    
    /* Gold Accent Text */
    .gold-accent {
        color: #fbbf24 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        text-align: center;
        font-size: 1.1rem;
    }
    
    /* Quote Styling */
    .premium-quote {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        color: #38bdf8 !important;
        font-size: 1.4rem;
        line-height: 1.6;
        margin: 25px 0;
    }
    
    .author-tag {
        color: #fbbf24 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 1rem;
    }
    
    /* Dhire-dhire sliding & opacity animation for Happy Birthday Anshika */
    .slow-reveal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        color: #ffffff;
        text-shadow: 0 0 15px rgba(236, 72, 153, 0.8);
        margin-top: 30px;
        opacity: 0;
        transform: translateY(20px);
        animation: smoothSlideUp 3.5s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    }
    
    @keyframes smoothSlideUp {
        0% { opacity: 0; transform: translateY(30px); filter: blur(5px); }
        40% { opacity: 0.3; }
        100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }
    
    /* Hidden native element controllers */
    .stDeployButton, footer, header {
        visibility: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Audio Core Engine
def play_system_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_html = f"""
                <audio autoplay="true" loop="true" style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Song file execution
play_system_audio("nastelbom-happy-birthday-49526.mp3")

# 4. Built-in Streamlit Animations (Balloons Aur Snowfall)
st.balloons()    # Har page load par automatically urenge balloons
st.snow()        # Pure background me dynamic crystal snow fall shuru ho jayega

# 5. Core Interface Construction
st.markdown('<div style="text-align: center; font-size: 2.5rem; margin-bottom: 10px;">✨ 🚀 ✨</div>', unsafe_allow_html=True)
st.markdown('<h1 class="cyber-title">A Celebration of Excellence</h1>', unsafe_allow_html=True)
st.markdown('<p class="gold-accent">📝 Dedicated to an exceptional mind on her special day 📝</p>', unsafe_allow_html=True)

# Sidebar photo matrix setup
st.sidebar.markdown("### 🌆 Media Control Matrix")
uploaded_image = st.sidebar.file_uploader("Upload Anshika's Premium Picture Here", type=["jpg", "png", "jpeg", "webp"])

# Main Luxury Card Container
st.markdown('<div class="luxury-card">', unsafe_allow_html=True)

# Render picture logic (with neon border wrap if image uploaded)
if uploaded_image is not None:
    st.image(uploaded_image, use_container_width=True)
else:
    # High-end temporary geometric banner if no pic uploaded yet
    st.markdown('<div style="font-size: 5rem; padding: 20px 0;">👑</div>', unsafe_allow_html=True)

# English Premium Quotes
st.markdown('<p class="premium-quote">"The future belongs to those who believe in the beauty of their dreams."</p>', unsafe_allow_html=True)
st.markdown('<p class="author-tag">— ELEANOR ROOSEVELT</p>', unsafe_allow_html=True)

st.markdown('<hr style="border-color: rgba(168, 85, 247, 0.3); ">', unsafe_allow_html=True)

# Paragraph appreciation message
st.markdown("""
<div style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; line-height: 1.8; text-align: center; color: #e2d9f3;">
It is a profound privilege to guide a student with your <span style="color: #38bdf8; font-weight: 600;">brilliant intellect</span>, 
relentless dedication, and unwavering curiosity. Your potential is absolutely limitless!
</div>
""", unsafe_allow_html=True)

# Custom dynamic CSS animation text at the absolute bottom inside card
st.markdown('<div class="slow-reveal">✨ Happy Birthday Anshika 🎂 ✨</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer Execution
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #6d5b86; font-family: \'Montserrat\', sans-serif; font-size: 0.8rem; font-weight: 600; letter-spacing: 2px;">'
    'POWERED BY PREMIUM STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

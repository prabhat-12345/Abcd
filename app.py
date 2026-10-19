import streamlit as st
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="For Anshika", 
    page_icon="💖", 
    layout="centered"
)

# 2. Perfect CSS (Fixing colors and background visibility)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* Strong soft gradient background */
    .stApp {
        background: linear-gradient(135deg, #ffeef4 0%, #ffd6e8 100%) !important;
    }
    
    /* Premium glass card with distinct border */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        border: 2px solid #e86d8a;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(232, 109, 138, 0.2);
        text-align: center;
        margin-top: 15px;
    }
    
    /* CRITICAL FIX: Dark striking text colors for visibility */
    .main-title {
        font-family: 'Dancing Script', cursive;
        color: #911b43 !important; /* Deep Crimson/Maroon */
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 5px;
        text-align: center;
    }
    
    .sub-title {
        font-family: 'Montserrat', sans-serif;
        color: #5c474e !important; /* Dark Charcoal Pink */
        font-size: 1.1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 600;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .quote-box {
        font-family: 'Montserrat', sans-serif;
        font-style: italic;
        color: #2b1f23 !important; /* Deep Dark for clean reading */
        font-size: 1.2rem;
        border-left: 4px solid #911b43;
        padding-left: 15px;
        margin: 20px 0;
        text-align: left;
        line-height: 1.6;
    }

    /* Beautiful animated Pure CSS Heart (No broken image links) */
    .heart-element {
        font-size: 80px;
        color: #d12857;
        animation: heartbeat 1.2s infinite;
        margin: 20px auto;
        text-align: center;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        20% { transform: scale(1.25); }
        40% { transform: scale(1); }
        60% { transform: scale(1.15); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# 3. Automatic Audio Function
def inject_premium_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            audio_bytes = f.read()
            audio_b64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
                <audio autoplay="true" loop="true" style="display:none;">
                <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

inject_premium_audio("nastelbom-happy-birthday-49526.mp3")

# 4. Content Render
st.balloons() # Automatic balloons on start

st.markdown('<div style="text-align: center; font-size: 2rem;">💖 ✨ 🕊️</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">Beautiful Anshika</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">A Journey of Moments & Love</p>', unsafe_allow_html=True)

# Sidebar setup for picture upload
st.sidebar.markdown("### 🛠️ Content Controls")
uploaded_file = st.sidebar.file_uploader(
    "Anshika ki photo yahan se upload karein 👇", 
    type=["jpg", "jpeg", "png", "webp"]
)

st.markdown('<div class="premium-card">', unsafe_allow_html=True)

# Agar user photo upload karega toh photo dikhegi, nahi toh dhadakta hua dil dikhega
if uploaded_file is not None:
    st.image(uploaded_file, use_container_width=True, caption="Elegance Personified ✨")
else:
    # Safe Animated fallback
    st.markdown('<div class="heart-element">❤️</div>', unsafe_allow_html=True)
    st.caption("ℹ️ Use Sidebar to upload Anshika's picture")

# English Quotes Text Box
st.markdown("""
<div class="quote-box">
    "In the arithmetic of love, one plus one equals everything, and two minus one equals nothing. 
    You are the rhythm to my silence and the sparkle in my ordinary days."
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: #785a63; font-family: \'Montserrat\', sans-serif; font-size: 0.85rem; font-weight: 600; letter-spacing: 1px;">'
    'DESIGNED WITH PREMIUM CODE STACKS FOR ANSHIKA'
    '</div>', 
    unsafe_allow_html=True
)

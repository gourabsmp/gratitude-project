import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="With Deepest Gratitude", page_icon="🙏", layout="centered")

# --- PREMIUM ELEGANT CSS ---
st.markdown("""
    <style>
    /* Import Elegant Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Source+Sans+Pro:wght@300;400;600&display=swap');

    /* Soft, Warm Background Gradient */
    .stApp {
        background: linear-gradient(120deg, #fdfbfb 0%, #f4f4f4 100%);
        color: #2b2b2b;
        font-family: 'Source Sans Pro', sans-serif;
    }
    
    /* Cinematic Fade-in Animation */
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .fade-in {
        animation: fadeInUp 1.2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }

    /* Typography */
    .main-title {
        font-family: 'Playfair Display', serif;
        color: #1a252f;
        text-align: center;
        font-size: 3.5em;
        font-weight: 700;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }
    .sub-title {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-style: italic;
        color: #7f8c8d;
        font-size: 1.3em;
        margin-bottom: 40px;
    }

    /* The Letter Box */
    .letter-box {
        background-color: #ffffff;
        padding: 45px 50px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        border-top: 4px solid #d4af37; /* Elegant Gold */
        font-size: 1.15em;
        line-height: 1.8;
        color: #34495e;
        margin-bottom: 40px;
    }
    
    /* Section Headers */
    .section-header {
        font-family: 'Playfair Display', serif;
        text-align: center; 
        color: #1a252f; 
        font-size: 2.2em;
        margin-bottom: 25px;
        margin-top: 20px;
    }

    /* Hero Cards for the Grid */
    .hero-card {
        background: #ffffff;
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #f0f2f5;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hero-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.15);
        border-color: #d4af37;
    }
    .hero-name {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1em;
    }
    .hero-dept {
        color: #95a5a6;
        font-size: 0.85em;
        margin-top: 6px;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Dubey Sir Special Tribute Box */
    .tribute-box {
        background: linear-gradient(135deg, #2c3e50 0%, #1a252f 100%);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-bottom: 4px solid #d4af37;
    }
    .tribute-title {
        font-family: 'Playfair Display', serif;
        color: #d4af37;
        font-size: 2em;
        margin-bottom: 10px;
    }
    .tribute-name {
        font-size: 1.5em;
        font-weight: 600;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }
    .tribute-text {
        font-size: 1.1em;
        line-height: 1.7;
        font-style: italic;
        color: #ecf0f1;
        max-width: 80%;
        margin: auto;
    }

    /* Interactive Button */
    .thank-you-btn > button {
        width: 100%; 
        background: linear-gradient(135deg, #d4af37 0%, #b5952f 100%);
        color: white;
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: 600; 
        font-size: 1.2em; 
        border-radius: 30px;
        border: none; 
        padding: 15px; 
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3);
    }
    .thank-you-btn > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.5);
    }
    .photo-caption {
        text-align: center; font-style: italic; color: #95a5a6;
        margin-top: 10px; margin-bottom: 25px; font-size: 0.9em;
    }
    
    /* Custom Gold Divider */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(212, 175, 55, 0), rgba(212, 175, 55, 0.5), rgba(212, 175, 55, 0));
        margin: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='fade-in'><h1 class='main-title'>To My Brothers</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='fade-in'><p class='sub-title'>Haldia Institute of Technology • Saraswati Puja Committee 2026</p></div>", unsafe_allow_html=True)

# --- THE LETTER ---
st.markdown("""
<div class='fade-in letter-box'>
    <p>Dear Friends,</p>
    <p>As you all know, my family recently received the difficult news of my father, Samir Singha Mahapatra's, Stage 1 cancer diagnosis. We have been preparing for his upcoming surgery on 6th March, and it has been a deeply challenging time emotionally and financially.</p>
    <p>When I found out that our Saraswati Puja Committee came together to contribute to his treatment fund, I was left completely speechless. In a world where everyone is busy fighting their own battles, you took the time and resources to help me fight mine.</p>
    <p>I wanted to share his medical updates here so you can see exactly how your generous contributions are giving my father hope. Your support is a powerful reminder that I am not alone.</p>
    <p>Thank you, from the bottom of my heart, for standing by me when I needed it the most.</p>
    <br>
    <p><i>With immense gratitude,</i><br>
    <b style='font-size: 1.1em;'>Gourab Singha Mahapatra</b><br>
    <span style='font-size: 0.85em; color: #7f8c8d; text-transform: uppercase; letter-spacing: 0.5px;'>Mechanical Engineering, Batch of 2019-2023</span></p>
</div>
""", unsafe_allow_html=True)

# --- MEDICAL UPDATES & TRANSPARENCY ---
st.markdown("<div class='fade-in'><h2 class='section-header'>Medical Updates & Treatment Plan</h2></div>", unsafe_allow_html=True)

col_rep1, col_rep2 = st.columns(2)
with col_rep1:
    if os.path.exists("prescription.jpeg"):
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.image("prescription.jpeg", use_container_width=True)
        st.markdown("<p class='photo-caption'>Surgery Scheduled for 6th March</p></div>", unsafe_allow_html=True)
with col_rep2:
    if os.path.exists("scan.jpeg"):
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.image("scan.jpeg", use_container_width=True)
        st.markdown("<p class='photo-caption'>Initial Eye Scan</p></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- GROUP PHOTO ---
st.markdown("<div class='fade-in'><h2 class='section-header'>Our Family</h2></div>", unsafe_allow_html=True)
if os.path.exists("group_photo.jpeg"):
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image("group_photo.jpeg", use_container_width=True)
    st.markdown("<p class='photo-caption'>Saraswati Puja 2026</p></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- THE WALL OF BROTHERHOOD ---
st.markdown("<div class='fade-in'><h2 class='section-header'>The Wall of Brotherhood</h2></div>", unsafe_allow_html=True)

# The Complete List of 13 Friends
friends = [
    {"name": "Rishav Kumar", "dept": "CSE AIML"},
    {"name": "Nishant Singh", "dept": "AEIE"},
    {"name": "Aatish Kumar", "dept": "IT"},
    {"name": "Rajdeep Sinha", "dept": "CSE CS"},
    {"name": "Abhinandan Kumar Singh", "dept": "ME"},
    {"name": "Tanay Srivastav", "dept": "CSE CS"},
    {"name": "Shubhanshu Kumar", "dept": "IT"},
    {"name": "Om Prakash Kumar", "dept": "ECE"},
    {"name": "Manish Kumar", "dept": "CSE AIML"},
    {"name": "Gaurav Kumar", "dept": "ECE"},
    {"name": "Chirag Sinha", "dept": "ME"},
    {"name": "Saksham", "dept": "CSE DS"},
    {"name": "Abhinav Anand", "dept": "CSE DS"}
]

cols = st.columns(3)
for index, friend in enumerate(friends):
    with cols[index % 3]:
        st.markdown(f"""
        <div class='fade-in hero-card'>
            <div class='hero-name'>{friend['name']}</div>
            <div class='hero-dept'>{friend['dept']}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- SPECIAL THANKS: DUBEY SIR ---
st.markdown("""
<div class='fade-in tribute-box'>
    <div class='tribute-title'>A Special Thanks</div>
    <div class='tribute-name'>To Dubey Sir</div>
    <div class='tribute-text'>
        For your unwavering support, guidance, and for standing by me and my family during one of our most difficult chapters. Your mentorship and kindness extend far beyond the classroom walls, and my family and I are deeply, truly grateful.
    </div>
</div>
""", unsafe_allow_html=True)

# --- INTERACTIVE GRATITUDE BUTTON ---
if 'thanked' not in st.session_state:
    st.session_state.thanked = False

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="fade-in thank-you-btn">', unsafe_allow_html=True)
    if st.button("Click to receive my thanks 🙏"):
        st.session_state.thanked = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.thanked:
    st.balloons()
    st.success("Thank you for being the greatest support system a person could ask for.")

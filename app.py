import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="With Deepest Gratitude", page_icon="🙏", layout="centered")

# --- CUSTOM WARM CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        color: #2b2b2b;
    }
    .main-title {
        font-family: 'Georgia', serif;
        color: #2c3e50;
        text-align: center;
        font-size: 3em;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-style: italic;
        color: #7f8c8d;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .letter-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-top: 5px solid #d4af37;
        font-size: 1.15em;
        line-height: 1.7;
        margin-bottom: 30px;
    }
    .hero-card {
        background: linear-gradient(135deg, #f1f2f6 0%, #ffffff 100%);
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #e1e5eb;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }
    .hero-name {
        font-weight: bold;
        color: #2c3e50;
        font-size: 1.1em;
    }
    .hero-dept {
        color: #7f8c8d;
        font-size: 0.85em;
        margin-top: 5px;
        font-weight: 500;
    }
    .thank-you-btn > button {
        width: 100%; background-color: #d4af37; color: white;
        font-weight: bold; font-size: 1.2em; border-radius: 8px;
        border: none; padding: 12px; transition: 0.3s;
    }
    .thank-you-btn > button:hover {
        background-color: #b5952f; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.4); transform: scale(1.02);
    }
    .photo-caption {
        text-align: center;
        font-style: italic;
        color: #7f8c8d;
        margin-top: 8px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='main-title'>To My Brothers</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Haldia Institute of Technology • Saraswati Puja Committee 2026</p>", unsafe_allow_html=True)

# --- THE LETTER ---
st.markdown("""
<div class='letter-box'>
    <p>Dear Friends,</p>
    <p>As you all know, my family recently received the difficult news of my father, Samir Singha Mahapatra's, Stage 1 cancer diagnosis. We have been preparing for his upcoming surgery on 6th March, and it has been a deeply challenging time emotionally and financially.</p>
    <p>When I found out that our Saraswati Puja Committee came together to contribute to his treatment fund, I was left completely speechless. In a world where everyone is busy fighting their own battles, you took the time and resources to help me fight mine.</p>
    <p>I wanted to share his medical updates here so you can see exactly how your generous contributions are giving my father hope. Your support is a powerful reminder that I am not alone.</p>
    <p>Thank you, from the bottom of my heart, for standing by me when I needed it the most.</p>
    <br>
    <p><i>With immense gratitude,</i><br><b>Gourab</b></p>
</div>
""", unsafe_allow_html=True)

# --- MEDICAL UPDATES & TRANSPARENCY (THE REPORTS) ---
st.markdown("<h2 style='text-align: center; color: #2c3e50; margin-bottom: 20px;'>Medical Updates & Treatment Plan</h2>", unsafe_allow_html=True)

col_rep1, col_rep2 = st.columns(2)
with col_rep1:
    if os.path.exists("prescription.jpg"):
        st.image("prescription.jpg", use_container_width=True)
        st.markdown("<p class='photo-caption'>Surgery Scheduled for 6th March</p>", unsafe_allow_html=True)
with col_rep2:
    if os.path.exists("scan.jpg"):
        st.image("scan.jpg", use_container_width=True)
        st.markdown("<p class='photo-caption'>Initial Eye Scan</p>", unsafe_allow_html=True)

st.divider()

# --- GROUP PHOTO ---
st.markdown("<h2 style='text-align: center; color: #2c3e50; margin-bottom: 20px;'>Our Family</h2>", unsafe_allow_html=True)
if os.path.exists("group_photo.jpg"):
    st.image("group_photo.jpg", use_container_width=True)
    st.markdown("<p class='photo-caption'>Saraswati Puja 2026</p>", unsafe_allow_html=True)

st.divider()

# --- THE WALL OF BROTHERHOOD ---
st.markdown("<h2 style='text-align: center; color: #2c3e50; margin-bottom: 20px;'>The Wall of Brotherhood</h2>", unsafe_allow_html=True)

# The Complete List of 13 Friends with their Departments
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

# Generate the 3-column grid
cols = st.columns(3)
for index, friend in enumerate(friends):
    with cols[index % 3]:
        st.markdown(f"""
        <div class='hero-card'>
            <div class='hero-name'>{friend['name']}</div>
            <div class='hero-dept'>{friend['dept']}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- INTERACTIVE GRATITUDE BUTTON ---
if 'thanked' not in st.session_state:
    st.session_state.thanked = False

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="thank-you-btn">', unsafe_allow_html=True)
    if st.button("Click to receive my thanks 🙏"):
        st.session_state.thanked = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.thanked:
    st.balloons()
    st.success("Thank you for being the greatest support system a person could ask for.")

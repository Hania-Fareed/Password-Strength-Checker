import streamlit as st
import re

def check_password_strength(password):
    feedback = []
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one number.")
    
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")
    
    return score, feedback

# Streamlit Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Page Title
st.markdown('<h1 style="font-size:36px;">🔐 Password Strength Checker</h1>', unsafe_allow_html=True)
st.markdown("""
<h3 style="font-size:24px;">Welcome to the Ultimate Password Strength Checker! 👋</h3>
<p style="font-size:18px;">Use this tool to check your password strength and get suggestions to improve security.</p>

<p style="font-size:18px;">💡 A <b>strong password</b> should be:</p>
<ul style="font-size:18px;">
<li>At least <b>8 characters long</b></li>
<li>Contain <b>uppercase & lowercase letters</b></li>
<li>Include <b>numbers</b></li>
<li>Have <b>special characters</b> (!@#$%^&*)</li>
</ul>
""", unsafe_allow_html=True)

# User Input
password = st.text_input("Enter your password", type="password")

# Strength Analysis
if password:
    score, feedback = check_password_strength(password)
    
    # Strength Bar
    st.markdown("<h3 style='font-size:24px;'>Password Strength</h3>", unsafe_allow_html=True)
    strength_colors = {0: "red", 1: "orange", 2: "yellow", 3: "blue", 4: "green"}
    strength_labels = {0: "Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong"}
    text_color = "black" if strength_colors[score] == "yellow" else "white"
    
    st.markdown(
        f'<div style="border-radius: 10px; padding: 10px; text-align: center; font-size: 24px; background-color: {strength_colors[score]}; color: {text_color};">{strength_labels[score]}</div>',
        unsafe_allow_html=True
    )
    
    # Feedback Section
    if score < 4:
        st.markdown("<h3 style='font-size:24px;'>Suggestions to Improve Your Password</h3>", unsafe_allow_html=True)
        for tip in feedback:
            st.markdown(f"<p style='font-size:18px;'>{tip}</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='font-size:18px;'>🔹 Enter your password to check its strength.</p>", unsafe_allow_html=True)

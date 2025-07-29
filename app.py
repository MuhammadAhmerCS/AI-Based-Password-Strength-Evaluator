import streamlit as st
import string

st.set_page_config(page_title="Password Strength Evaluator", layout="centered")
st.title("🔐 AI-Based Password Strength Evaluator")

# Input field
password = st.text_input("Enter a password:")

# Rule-based evaluator function
def evaluate_password(pwd):
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in string.punctuation for c in pwd)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    # Simple rule-based classification
    if length < 6 or score < 2:
        return "Weak"
    elif length >= 6 and score == 2:
        return "Medium"
    elif length >= 8 and score >= 3:
        return "Strong"
    else:
        return "Medium"

# Output
if password:
    strength = evaluate_password(password)
    st.write("You entered:", password)
    st.info(f"Password Strength: **{strength}**")

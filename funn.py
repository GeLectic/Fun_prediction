import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r'random_forest_model.pkl')

# Set page configuration
st.set_page_config(page_title="Ladki Milne Ka Predictor", layout="wide")

# App Title with Image
st.title("Ladki Milne Ka Percentage")
st.markdown("""
    Enter your details below to find out your chances of success!
    * This  is a fun project/webapp but the data used in this was real :).*
""")




col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=25, step=1)
    height = st.number_input("Height (cm)", min_value=140, max_value=220, value=170, step=1)
with col2:
    looks_rating = st.slider("Looks Rating (1-10)", min_value=1, max_value=10, value=5)
    confidence_level = st.slider("Confidence Level (1-10)", min_value=1, max_value=10, value=5)


st.write("### Select Your Hobbies")
hobbies = st.multiselect(
    "Choose Your Hobbies",
    ["Cooking", "Dancing", "Gaming", "Music", "Reading", "Sports", "Traveling"],
    default=["Music", "Gaming"]
)


st.write("### Select Your Personality Type")
personality = st.radio("Personality Type", ["Ambivert", "Extrovert", "Introvert"])


personality_ambivert = 1 if personality == "Ambivert" else 0
personality_extrovert = 1 if personality == "Extrovert" else 0
personality_introvert = 1 if personality == "Introvert" else 0


input_features = np.array([
    age, looks_rating, confidence_level, height,
    int("Cooking" in hobbies), int("Dancing" in hobbies), int("Gaming" in hobbies),
    int("Music" in hobbies), int("Reading" in hobbies), int("Sports" in hobbies),
    int("Traveling" in hobbies), personality_ambivert, personality_extrovert,
    personality_introvert
]).reshape(1, -1)


if st.button("Predict"):
    prediction = model.predict(input_features)[0] * 100  # Convert to percentage
    st.markdown(f"### Your chances are: **{prediction:.2f}%** 💯 **ki ladki milegi!**")
    if prediction > 70:
        st.balloons()
    elif prediction < 50:
        st.warning("Milegi bhai Teko bhi jald he kabhi na kabhi milegi chutttt! 💪")


st.markdown("___")
st.markdown("Developed by the Poha for the Indori Pohaa ❤️")

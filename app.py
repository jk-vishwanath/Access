import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('lead_score_model.pkl')

# Streamlit App
st.title("Lead Score Prediction")

st.write("Enter the details below to predict the lead score.")

# Input fields for user to enter data
classification = st.selectbox("Classification", ["CXO/ Founder", "Investor", "Other", "Working Professional", "Researcher", "Student"])
industry = st.selectbox("Industry", ["Technology & AI", "Healthcare", "Finance", "Other"])
funding_stage = st.selectbox("Funding Stage", ["Pre-Seed", "Seed", "Round A+", "Other"])

# Create a dictionary for one-hot encoding
input_data = {
    "Classification_CXO/ Founder": classification == "CXO/ Founder",
    "Industry_Technology & AI": industry == "Technology & AI",
    "funding_stage_filled_Round A+": funding_stage == "Round A+"
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

if st.button("Predict Lead Score"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Lead Score: {prediction[0]:.2f}")

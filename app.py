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
    "Classification_Investors": classification == "Investors",
    "Classification_Researcher": classification == "Research", 
    "Classification_Student": classification == "Student", 
    "Classification_Other": classification == "Other", 
    "Industry_Healthcare": industry == "Healthcare", 
    "Industry_Finance": industry == "Finance", 
    "Industry_Other": == "Other", 
    "Industry_Technology & AI": industry == "Technology & AI",
    "funding_stage_filled_Round A+": funding_stage == "Round A+"
    "funding_stage_filled_Pre-Seed": funding_stage == "Pre-Seed"
    "funding_stage_filled_Seed": funding_stage == "Seed"
    "funding_stage_filled_Other": funding_stage == "Other"

}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

if st.button("Predict Lead Score"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Lead Score: {prediction[0]:.2f}")

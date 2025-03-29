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
    "Industry_Other": industry == "Other", 
    "Industry_Technology & AI": industry == "Technology & AI",
    "funding_stage_Round A+": funding_stage == "Round A+",
    "funding_stage_Pre-Seed": funding_stage == "Pre-Seed",
    "funding_stage_Seed": funding_stage == "Seed",
    "funding_stage_Other": funding_stage == "Other"

}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

input_df.columns = [col.replace('Pre-seed', 'Pre-Seed') for col in input_df.columns]

for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[model.feature_names_in_]

input_df = input_df.astype(float)  # Convert all numeric features to float


if st.button("Predict Lead Score"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Lead Score: {prediction[0]:.2f}")

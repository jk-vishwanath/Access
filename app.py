import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('lead_score_model.pkl')

# Streamlit App
st.title("Lead Score Prediction")

st.write("Enter the details below to predict the lead score.")

# Input fields for user to enter data
classification = st.selectbox("Classification", [
    "CXO/ Founder", "Investors", "Researcher", "Student", "Working Professional", "CTO"
])
industry = st.selectbox("Industry", [
    "Business Services", "Business Strategy and Operations", "Consumer & Retail", 
    "Education & Events", "Energy", "Finance & Fintech", "Health & Wellness", 
    "Human Resources", "InsurTech", "Investment", "Legal", "Media & Entertainment", 
    "Real Estate", "Religious Organizations", "Sales & Marketing", 
    "Sustainability & Climate", "Technology & AI", "Telecommunications", 
    "Travel & Logistics"
])
funding_stage = st.selectbox("Funding Stage", [
    "Non-Profit", "Pre-seed", "Seed", "Round A+", "Bootstrapping", "Missing"
])

# Create a dictionary for one-hot encoding
input_data = {col: 0 for col in model.feature_names_in_}  # Initialize with zeros

# Set appropriate values based on user input
input_data[f"Classification_{classification}"] = 1
input_data[f"Industry_{industry}"] = 1
input_data[f"funding_stage_{funding_stage}"] = 1
input_data[f"funding_stage_filled_{funding_stage}"] = 1  # Ensure both variants are handled

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Ensure all columns match the model's expected feature names
input_df = input_df[model.feature_names_in_]

# Convert all numeric features to float
input_df = input_df.astype(float)

# Predict when button is clicked
if st.button("Predict Lead Score"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Lead Score: {prediction[0]:.2f}")

import streamlit as st
import pickle
import numpy as np

with open('stroke_prediction_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


st.set_page_config(page_title="Stroke Prediction App", page_icon="🩺", layout="centered")
st.title("🩺 Stroke Prediction App")
st.write("""
This app predicts the likelihood of stroke based on your health and lifestyle information. 
Please provide the details below to get your prediction. 
""")


st.header("Input Your Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.radio("Gender", ["Male", "Female"], index=1)
    age = st.slider("Age", 0, 100, 25, help="Select your age in years.")
    hypertension = st.radio("Do you have Hypertension?", ["No", "Yes"], index=0)
    heart_disease = st.radio("Do you have Heart Disease?", ["No", "Yes"], index=0)

with col2:
    ever_married = st.radio("Have you ever been married?", ["No", "Yes"], index=0)
    work_type = st.selectbox(
        "Work Type", 
        ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"],
        help="Select your current work type."
    )
    residence_type = st.radio("Residence Type", ["Urban", "Rural"], index=0)
    smoking_status = st.selectbox(
        "Smoking Status", 
        ["never smoked", "formerly smoked", "smokes", "Unknown"],
        help="Select your smoking habit status."
    )

avg_glucose_level = st.number_input(
    "Average Glucose Level (mg/dL)", 
    min_value=0.0, 
    max_value=300.0, 
    step=0.1, 
    help="Enter your average glucose level."
)
bmi = st.number_input(
    "BMI (Body Mass Index)", 
    min_value=0.0, 
    max_value=100.0, 
    step=0.1, 
    help="Enter your BMI (e.g., 25.5)."
)

# Preprocessing the inputs to match the model's training pipeline
def encode_inputs():
    return [
        1 if gender == "Male" else 0, 
        age,
        1 if hypertension == "Yes" else 0,  
        1 if heart_disease == "Yes" else 0, 
        1 if ever_married == "Yes" else 0, 
        ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"].index(work_type),
        1 if residence_type == "Urban" else 0, 
        avg_glucose_level,
        bmi,
        ["never smoked", "formerly smoked", "smokes", "Unknown"].index(smoking_status),
    ]

input_data = np.array([encode_inputs()])

# Prediction Button 
if st.button("💡 Predict"):
    prediction = loaded_model.predict(input_data)
    result = "⚠️ High Stroke Risk!" if prediction[0] == 1 else "✅ Low Stroke Risk!"
    
   
    st.subheader("Prediction Result:")
    st.success(result if prediction[0] == 0 else result)
    if prediction[0] == 1:
        st.warning(
            "It's advised to consult a healthcare provider for further guidance. "
        )


st.write("---")
st.markdown(
    """
    **Disclaimer:** This app is for informational purposes only and not a substitute for professional medical advice. 
    """
)

# 🩺 Stroke Prediction App

Welcome to the **Stroke Prediction App**, a web application designed to predict the likelihood of a stroke based on user-provided health and lifestyle information. This project uses a **Random Forest Classifier** trained on a healthcare dataset to provide insights and predictions.

## 🌐 Live Demo
Check out the live app on Streamlit: [Stroke Prediction App](https://ish-stroke-predict.streamlit.app/)

---

## 📖 About the Project

Stroke is one of the leading causes of death and long-term disability worldwide. Early prediction can help in taking preventative measures. This app:
- Accepts user inputs such as age, BMI, smoking status, and more.
- Uses a trained machine learning model to predict the risk of stroke.
- Provides user-friendly UI/UX for seamless interaction.

---

## 🚀 Features
- **Intuitive UI/UX**: Enhanced user interface with Streamlit.
- **Machine Learning Model**: Trained using a Random Forest Classifier.
- **Dynamic Input Fields**: Inputs are validated and preprocessed before prediction.
- **Health Insights**: Displays results and advises on high-risk predictions.

---

## ⚙️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn, Random Forest Classifier
- **Deployment**: Streamlit Cloud

---

## 🛠️ How to Use the App
1. Visit the live app: [Stroke Prediction App](https://ish-stroke-predict.streamlit.app/).
2. Fill in the required fields such as age, gender, smoking status, etc.
3. Click the **Predict** button.
4. View the prediction result:
   - ✅ **Low Stroke Risk**
   - ⚠️ **High Stroke Risk**

---

## 📊 Dataset
Kaggle Dataset - https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

---

## 🛠️ How to Run Locally

### Prerequisites
1. Python 3.8+
2. Required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Clone the Repository
```bash
git clone https://github.com/iiTzIsh/Stroke-Prediction_App.git
cd Stroke-Prediction_App
```

### Run the App Locally
```bash
streamlit run app.py
```
Open the provided URL in your browser to access the app locally.

---

## 🧑‍💻 Author
Developed with ❤️ by [iiTzIsh](https://github.com/iiTzIsh).

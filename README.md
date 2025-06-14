# 🎯 Student Score Predictor

This is a simple **Streamlit web app** that uses **Linear Regression** to predict student exam scores based on the number of hours studied.

## 📌 Features
- Input study hours (0 to 24)
- Predict expected marks
- Powered by Scikit-learn
- Interactive Streamlit interface

## 📷 Demo Screenshot
![screenshot](screenshot.png) <!-- Add if you want -->

## 🚀 Tech Stack
- Python
- Streamlit
- Pandas
- Scikit-learn (Linear Regression)

## 🧠 How It Works
1. A dataset is created with study hours and corresponding marks
2. A Linear Regression model is trained
3. User inputs study hours
4. App predicts marks using the trained model

## 💡 Run It Locally

```bash
pip install streamlit pandas scikit-learn
streamlit run app.py

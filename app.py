import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("📚 Student Score Predictor")
st.write("Enter study hours to predict expected marks using Linear Regression.")

# Training data
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75]
}
df = pd.DataFrame(data)

# Train model
X = df[["Hours"]]
y = df["Marks"]
model = LinearRegression()
model.fit(X, y)

# User input
hours = st.number_input("Enter study hours", min_value=0.0, max_value=24.0, step=0.5)

# Predict button
if st.button("Predict Marks"):
    result = model.predict([[hours]])
    st.success(f"🎯 Estimated Marks: {result[0]:.2f}")

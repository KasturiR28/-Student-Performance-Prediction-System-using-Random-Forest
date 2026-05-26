import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("model.pkl")

# Page Config
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Prediction System")

st.write("Predict student performance using Machine Learning")

# Sidebar
st.sidebar.header("Enter Student Details")

# Inputs
study_hours = st.sidebar.slider(
    "Study Hours",
    1,
    12,
    5
)

attendance = st.sidebar.slider(
    "Attendance (%)",
    40,
    100,
    75
)

sleep_hours = st.sidebar.slider(
    "Sleep Hours",
    4,
    10,
    7
)

previous_marks = st.sidebar.slider(
    "Previous Marks",
    35,
    100,
    60
)

# Prediction Button
if st.button("Predict Performance"):

    input_data = np.array([
        [
            study_hours,
            attendance,
            sleep_hours,
            previous_marks
        ]
    ])

    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.success(
        f"Student Performance: {prediction[0]}"
    )

# Divider
st.markdown("---")

# Dataset Section
st.header("📊 Dataset Visualization")

# Load Dataset
df = pd.read_csv("student_data.csv")

# Show Dataset
if st.checkbox("Show Dataset"):

    st.write(df)

# Graph
fig, ax = plt.subplots()

ax.scatter(
    df['StudyHours'],
    df['PreviousMarks']
)

ax.set_xlabel("Study Hours")
ax.set_ylabel("Previous Marks")
ax.set_title("Study Hours vs Previous Marks")

st.pyplot(fig)

# Statistics
st.header("📈 Dataset Statistics")

st.write(df.describe())
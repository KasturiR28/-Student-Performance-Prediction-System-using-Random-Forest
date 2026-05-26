import pandas as pd
import random

# Number of rows
rows = 1000

# Empty list
data = []

for _ in range(rows):

    study_hours = random.randint(1, 12)
    attendance = random.randint(40, 100)
    sleep_hours = random.randint(4, 10)
    previous_marks = random.randint(35, 95)

    # Score calculation
    score = (
        study_hours * 3
        + attendance * 0.3
        + sleep_hours * 2
        + previous_marks * 0.5
        + random.randint(-5, 5)
    )

    # Performance Category
    if score >= 85:
        performance = "Excellent"
    elif score >= 70:
        performance = "Good"
    elif score >= 50:
        performance = "Average"
    else:
        performance = "Poor"

    data.append([
        study_hours,
        attendance,
        sleep_hours,
        previous_marks,
        performance
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'StudyHours',
    'Attendance',
    'SleepHours',
    'PreviousMarks',
    'Performance'
])

# Save CSV
df.to_csv('student_data.csv', index=False)

print("Dataset Generated Successfully")
print(df.head())
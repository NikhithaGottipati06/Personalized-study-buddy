import pandas as pd
import random

# Defining possible values for each column
patterns = ["Improving", "Consistent", "Declining"]
learning_speeds = ["Fast", "Average", "Slow"]
subjects = ["Math", "Science", "English", "History", "Geography"]
grades = ["A", "B", "C", "D", "F"]
revision_habits = ["Y", "N"]

# Generate 1000 rows of data
data = []

for i in range(1, 1001):
    score = random.randint(30, 100)  # Scores between 30 and 100
    grade = grades[(score // 20) - 1]  # Simple logic to assign grades based on score
    pattern = random.choice(patterns)
    learning_speed = random.choice(learning_speeds)
    subject = random.choice(subjects)
    revision_habit = random.choice(revision_habits)
    final_marks = round(score * random.uniform(0.8, 1.2))  # A variation of score to simulate final marks
    
    data.append([i, score, grade, pattern, learning_speed, subject, revision_habit, final_marks])

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=["S.No", "Scores", "Grades", "Pattern", "Learning Speed", "Subjects", "Revision Habits", "Final Marks"])

# Save to a CSV file
df.to_csv("exam_performance_dataset.csv", index=False)

# Display the first few rows
print(df.head())










import pandas as pd
import random

# Defining possible values for each column
study_frequencies = ["Daily", "Weekly", "Bi-weekly", "Monthly"]
study_subjects = ["Math", "Science", "English", "History", "Geography"]
study_types = ["Self-study", "Group study", "Online courses", "Tutoring"]
revision_frequencies = ["Daily", "Weekly", "Never"]
difficulty_levels = ["Easy", "Medium", "Hard"]

# Generate 1000 rows of data
data = []

for i in range(1, 1001):
    study_hours = random.randint(1, 8)  # Study hours between 1 and 8
    study_frequency = random.choice(study_frequencies)
    study_subject = random.choice(study_subjects)
    study_type = random.choice(study_types)
    revision_frequency = random.choice(revision_frequencies)
    difficulty_level = random.choice(difficulty_levels)
    track_of_hours = random.randint(5, 50)  # Total study hours in the past week
    
    data.append([i, study_hours, study_frequency, study_subject, study_type, revision_frequency, difficulty_level, track_of_hours])

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=["S.No", "Study Hours", "Study Frequency", "Study Subjects", "Study Type", "Revision Frequency", "Difficulty Level", "Track of Hours"])

# Save to a CSV file
df.to_csv("study_habits_dataset.csv", index=False)

# Display the first few rows
print(df.head())







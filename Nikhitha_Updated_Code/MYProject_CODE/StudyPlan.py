import streamlit as st
import pandas as pd
import random
import base64

st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"Study Plan"}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
add_bg_from_local('s1.jpg')    
    






# Function to adjust study plan dynamically
def adjust_study_plan(study_data):
    # Sort topics by time spent, prioritize less studied topics
    study_data['Adjusted Study Hours'] = study_data['Study Hours'] + (study_data['Max Study Time'] - study_data['Study Hours']) * 0.5
    return study_data

# Generate random study data
def generate_study_data():
    topics = ["Math", "Science", "English", "History", "Geography"]
    study_data = []

    for topic in topics:
        study_hours = random.randint(1, 4)  # Initial study hours between 1 and 4
        max_study_time = random.randint(3, 6)  # Maximum study time to be assigned later
        study_data.append([topic, study_hours, max_study_time])

    df = pd.DataFrame(study_data, columns=["Topic", "Study Hours", "Max Study Time"])
    return df

# Title and Instructions
# st.title("Study Plan Adjuster")
st.write("""
    Welcome to the dynamic Study Plan tool! This tool helps to adjust your study schedule based on how much time you’ve spent on different topics.
    You can enter your study hours for each topic, and the tool will update your schedule accordingly.
""")

# Generate initial study plan (example)
study_df = generate_study_data()

# Display the current study data
st.subheader("Current Study Plan")
st.write(study_df)

# Allow users to input their actual study hours for each topic
# st.subheader("Enter your actual study hours")
# study_df['Actual Study Hours'] = study_df['Study Hours']

# # Input fields for each topic
# for i in range(len(study_df)):
#     study_df.at[i, 'Actual Study Hours'] = st.number_input(f"Time spent on {study_df['Topic'][i]}", 
#                                                           min_value=0, max_value=12, value=study_df['Study Hours'][i], key=f"{i}")
st.subheader("Enter your actual study hours")

# Use session_state to persist user inputs across reruns
if 'actual_hours' not in st.session_state:
    st.session_state.actual_hours = dict(zip(study_df['Topic'], study_df['Study Hours']))

# Input fields for each topic, values stored in session_state
for i in range(len(study_df)):
    topic = study_df.at[i, 'Topic']
    st.session_state.actual_hours[topic] = st.number_input(
        f"Time spent on {topic}",
        min_value=0,
        max_value=12,
        value=st.session_state.actual_hours[topic],
        key=topic
    )
    study_df.at[i, 'Actual Study Hours'] = st.session_state.actual_hours[topic]
# Update the study plan dynamically
if st.button("Adjust Study Plan"):
#     # Adjust study plan based on input
#     study_df['Study Hours'] = study_df['Actual Study Hours']
#     adjusted_study_df = adjust_study_plan(study_df)

#     # Show the adjusted study plan
#     st.subheader("Adjusted Study Plan")
#     st.write(adjusted_study_df)

# # Display the original vs adjusted plan
# st.subheader("Original vs Adjusted Plan")
# comparison_df = pd.DataFrame({
#     "Topic": study_df['Topic'],
#     "Original Study Hours": study_df['Study Hours'],
#     "Adjusted Study Hours": adjusted_study_df['Adjusted Study Hours']
# })
# st.write(comparison_df)
    # Adjust study plan based on input
    study_df['Study Hours'] = study_df['Actual Study Hours']
    adjusted_study_df = adjust_study_plan(study_df)

    # Show the adjusted study plan
    st.subheader("Adjusted Study Plan")
    st.write(adjusted_study_df)

    # Display the original vs adjusted plan
    st.subheader("Original vs Adjusted Plan")
    comparison_df = pd.DataFrame({
        "Topic": study_df['Topic'],
        "Original Study Hours": study_df['Study Hours'],
        "Adjusted Study Hours": adjusted_study_df['Adjusted Study Hours']
    })
    st.write(comparison_df)


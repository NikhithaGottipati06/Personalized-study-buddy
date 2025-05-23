# ---------------- IMPORT PACKAGES 

import streamlit as st
from PIL import Image
import re
import numpy as np

# Function to extract text from the uploaded PDF
import base64

import pandas as pd
import sqlite3
from streamlit_option_menu import option_menu


# ================ Background image ===

st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"🧠📋Automated Answer Evaluation Using Deep Learning"}</h1>', unsafe_allow_html=True)


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
add_bg_from_local('1.jpg')




# selected = option_menu(
#     menu_title=None, 
#     options=["Mark Evaluate","Feedbacks"],  
#     orientation="horizontal",
# )


st.markdown(
    """
    <style>
    .option_menu_container {
        position: fixed;
        top: 20px;
        right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# if selected == 'Mark Evaluate':

    
    
import streamlit as st

# Define your questions and expected keywords for evaluation
questions = [
    {
        "question": "1. What is Machine Learning?",
        "keywords": ["algorithm", "data", "learn", "model", "pattern"]
    },
    {
        "question": "2. Explain the difference between Supervised and Unsupervised Learning.",
        "keywords": ["labeled", "unlabeled", "classification", "clustering", "training data"]
    },
    {
        "question": "3. What is Overfitting in Machine Learning?",
        "keywords": ["training data", "high accuracy", "low test accuracy", "complex model", "generalize"]
    }
]

# UI layout
st.markdown("### 🎯 **Paste your answers below. Marks will be estimated based on key concepts mentioned.**")

# Initialize score
total_score = 0
max_score = len(questions) * 5  # Each question is worth 5 marks

# Loop through questions
for idx, q in enumerate(questions):
    st.markdown(f"---\n#### ❓ {q['question']}")
    user_answer = st.text_area("✍️ Your Answer:", key=f"answer_{idx}", height=150)

    # Scoring
    if user_answer.strip():
        matched_keywords = [kw for kw in q["keywords"] if kw.lower() in user_answer.lower()]
        score = len(matched_keywords)  # 1 mark per keyword
        total_score += score

        # Show matched keywords
        st.markdown(f"✅ **Matched Keywords:** `{', '.join(matched_keywords)}`")
        st.markdown(f"📊 **Score for this answer:** <span style='color:green; font-size:18px;'>`{score}/5`</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color:red;'>❌ Answer is empty. Please provide an answer to receive marks.</span>", unsafe_allow_html=True)

# Final result after all questions
st.markdown("---")
if st.button("📩 Submit for Evaluation"):
    performance = "Excellent 🎉" if total_score >= 12 else "Good 👍" if total_score >= 7 else "Needs Improvement 🛠️"
    
    st.markdown(f"""
    ## 🏁 Final Evaluation
    - 📝 **Total Score:** <span style='color:blue; font-size:20px;'>`{total_score}/{max_score}`</span>
    - 🏆 **Performance:** <span style='color:green; font-size:18px;'>{performance}</span>
    """, unsafe_allow_html=True)

    st.balloons()


    

# if selected == 'Feedbacks':
    
#     st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"Feedbacks Using Reinforcement System"}</h1>', unsafe_allow_html=True)

#     def add_bg_from_local(image_file):
#         with open(image_file, "rb") as image_file:
#             encoded_string = base64.b64encode(image_file.read())
#         st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#             background-size: cover
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#         )
#     add_bg_from_local('1.jpg')
    
    
#     import streamlit as st
    
#     # Initial state (marks per question are set to 2)
#     initial_marks_per_question = 2
#     total_questions = 5  # Number of questions
    
#     # Define feedback options
#     feedd = ['For Key Word Missing, the system can reduce the marks', 
#              'Your Content Quality is not good', 
#              'Grammatical Mistake']
    
#     # Function to ask a question and allow the user to choose an option
#     def ask_question(question_number):
#         """ Simulate asking a question in Streamlit. """
#         st.write(f"**Question {question_number}**")
#         # Provide a unique key for each radio widget based on the question number
#         option = st.radio("Choose an option", ["Own Marks", "Feedback"], key=f"radio_{question_number}")
#         return option
    
#     # Function to let the user provide feedback and handle the feedback
#     def provide_user_feedback(question_number):
#         """ Let the user provide their own feedback. """
#         # Use modulo to wrap question_number within the bounds of the feedd list
#         feedback_index = (question_number - 1) % len(feedd)  # Wrap around if the question number exceeds list length
#         st.write("For Key Word Missing, the system can reduce the marks")
        
#         st.write(feedd[feedback_index])  # Safely access the feedback options
    
#         # Use the question number directly to create a unique key for each feedback
#         feedback = st.text_input(f"Please enter your feedback for Question {question_number}:", key=f"feedback_{question_number}")
#         if feedback:
#             st.write(f"Feedback received: '{feedback}'")
#         return feedback
    
#     # Function to update marks based on the user's actions for each question
#     def update_marks(action, current_marks, question_number):
#         """ Update marks based on the action chosen by the user. """
#         if action == "Own Marks":
#             # If the user chooses to see their own marks, they don't get an immediate change
#             st.write(f"Your current marks: {current_marks}")
#             return current_marks  # Marks stay the same
#         elif action == "Feedback":
#             # If the user chooses feedback, their score will decrease by 1
#             feedback = provide_user_feedback(question_number)  # Let the user enter their feedback
#             if feedback:
#                 st.write("Thank you for your feedback!")
#                 # Reduce marks by 1, but ensure they don't go below 0
#                 new_marks = max(current_marks - 1, 0)  
#                 st.write(f"After your feedback, your new marks: {new_marks}")
#                 return new_marks  # Marks decrease
#             else:
#                 st.warning("Please enter feedback before submitting.")
#                 return current_marks
    
#     # Main function to run the system and calculate total marks
#     def run_system():
#         total_marks = 0  # Initialize the total marks to 0
        
#         for question_number in range(1, total_questions + 1):
#             # Start with 2 marks per question
#             current_marks = initial_marks_per_question
            
#             action = ask_question(question_number)
            
#             # Update marks based on the action and feedback
#             current_marks = update_marks(action, current_marks, question_number)
            
#             # Add the current marks to the total marks
#             total_marks += current_marks
            
#             # Add a separator between questions for better visualization
#             st.markdown("---")
        
#         # Display the final total marks after all questions
#         st.write(f"**Total Marks after all questions:** {total_marks}")
    
#     # Streamlit app starts here
#     st.write("Welcome to the feedback system. You will go through all questions and choose whether to see your own marks or provide feedback.")
    
#     run_system()



    







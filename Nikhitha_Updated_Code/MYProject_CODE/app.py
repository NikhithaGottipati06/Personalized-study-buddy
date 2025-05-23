# ================ Input Packages =========================

import streamlit as st

import base64
import matplotlib.image as mpimg
import cv2

import matplotlib.pyplot as plt 
from streamlit_option_menu import option_menu
import numpy as np

# ================ Background image ==============================


st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Al-Powered Personalized Learning & Exam Performance Predictor"}</h1>', unsafe_allow_html=True)


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
add_bg_from_local('1.avif')


selected = option_menu(
    menu_title=None, 
    options=["Exam Score Prediction","Assesment Data","Study Plan","Note Summarization","Answer Evaluation","Q&A"],  
    orientation="horizontal",
)



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


import pandas as pd

data_frame=pd.read_csv("StudentData.csv")
       
gen = data_frame['gender'].unique()

idd = data_frame['StageID'].unique()

gid = data_frame['GradeID'].unique()


sid = data_frame['SectionID'].unique()

top = data_frame['Topic'].unique()

sem = data_frame['Semester'].unique()

stu = data_frame['StudentAbsenceDays'].unique()



if selected == "Exam Score Prediction":
    
    import streamlit as st
    import datetime
    
    # Function to calculate the score prediction
    def predict_score(avg_score, time_spent):
        predicted_score = avg_score * (1 + 0.1 * (time_spent / 60))  # Predicting with some logic
        return predicted_score
    
    # Function to calculate time spent in hours based on number of questions answered
    def calculate_time_spent(questions_answered):
        # Assuming it takes an average of 2 minutes per question
        time_spent_minutes = questions_answered * 2
        time_spent_hours = time_spent_minutes / 60
        return time_spent_hours
    
    # Title and description with markdown and icons
    # st.markdown("# 📚 Student Test Performance Prediction")
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"📚 Student Test Performance Prediction"}</h1>', unsafe_allow_html=True)

    st.markdown("Welcome to the **Student Performance Predictor**! Fill in the details below to predict your future score.")
    
    # Input for the scores for previous tests (at least 6 questions per test)
    st.markdown("## 📊 Previous Test Scores (Each test contains at least 6 questions)")
    
    # Input for Test 1
    test_1_score = st.number_input("1️⃣ Previous Test 1 Score", min_value=0, max_value=100, value=75)
    test_1_questions = st.number_input("Number of questions answered in Test 1", min_value=6, value=6)
    
    # Input for Test 2
    test_2_score = st.number_input("2️⃣ Previous Test 2 Score", min_value=0, max_value=100, value=80)
    test_2_questions = st.number_input("Number of questions answered in Test 2", min_value=6, value=6)
    
    # Input for Test 3
    test_3_score = st.number_input("3️⃣ Previous Test 3 Score", min_value=0, max_value=100, value=85)
    test_3_questions = st.number_input("Number of questions answered in Test 3", min_value=6, value=6)
    
    # Calculate the average score from previous tests
    avg_score = (test_1_score + test_2_score + test_3_score) / 3
    
    # Calculate total time spent based on questions answered
    time_spent_test_1 = calculate_time_spent(test_1_questions)
    time_spent_test_2 = calculate_time_spent(test_2_questions)
    time_spent_test_3 = calculate_time_spent(test_3_questions)
    
    total_time_spent = time_spent_test_1 + time_spent_test_2 + time_spent_test_3
    
    # Display the calculated average score and time spent
    st.markdown(f"### Average Score from Previous Tests: {avg_score:.2f}")
    st.markdown(f"### Total Time Spent: {total_time_spent:.2f} hours")
    
    # Predict the score based on average score and time spent
    predicted_score = predict_score(avg_score, total_time_spent)
    
    st.markdown(f"## 🔮 Predicted Score for Next Test: {predicted_score:.2f}")
    
    # Displaying the conclusion with an icon
    st.markdown("""
    ---
    ### 🎯 Conclusion:
    Based on your performance in previous tests and the time spent, your predicted score for the next test is **{:.2f}**.
    Good luck! Keep practicing! 💪
    """.format(predicted_score))

            
        
if selected=="Assesment Data": 
        
    import streamlit as st
    
    # List of subjects
    subjects = ["Python", "Data Science", "Java", "Machine Learning", "AI"]
    
    import streamlit as st

# List of subjects

    # Predefined MCQs for each subject
    questions_data = {
        "Python": [
            {"question": "What is the output of `print(2 + 2)`?", "options": ["4", "5", "3", "Error"], "answer": "4"},
            {"question": "Which of the following is a mutable data type?", "options": ["String", "List", "Tuple", "Set"], "answer": "List"},
            {"question": "Which function is used to get the length of a list?", "options": ["len()", "length()", "count()", "size()"], "answer": "len()"},
            {"question": "What does `len()` do?", "options": ["Counts items", "Returns length of object", "Returns size of object", "Removes items"], "answer": "Returns length of object"},
            {"question": "What does `None` represent?", "options": ["True", "False", "Null value", "Zero"], "answer": "Null value"},
            {"question": "How do you start a comment in Python?", "options": ["#", "//", "/*", "/*...*/"], "answer": "#"},
            {"question": "Which operator is used to compare two values in Python?", "options": ["=", "==", "=", "!="], "answer": "=="},
            {"question": "Which method is used to add an item to the end of a list?", "options": ["add()", "append()", "insert()", "extend()"], "answer": "append()"},
            {"question": "Which of the following is an immutable type?", "options": ["List", "Set", "String", "Dictionary"], "answer": "String"},
            {"question": "Which of the following is used for iteration in Python?", "options": ["for loop", "while loop", "range()", "all of the above"], "answer": "all of the above"}
        ],

        "Data Science": [
            {"question": "What is Data Science?", "options": ["Study of data", "Data cleaning", "Data mining", "All of the above"], "answer": "All of the above"},
            {"question": "Which library is used for data manipulation in Python?", "options": ["Matplotlib", "NumPy", "Pandas", "Seaborn"], "answer": "Pandas"},
            {"question": "Which of the following is used for machine learning?", "options": ["Matplotlib", "Scikit-learn", "TensorFlow", "Both B and C"], "answer": "Both B and C"},
            {"question": "What is a DataFrame?", "options": ["2D array", "1D array", "Table-like structure", "None of the above"], "answer": "Table-like structure"},
            {"question": "Which algorithm is used for classification?", "options": ["Linear regression", "Logistic regression", "K-means", "KNN"], "answer": "Logistic regression"},
            {"question": "Which of the following is a visualization library?", "options": ["NumPy", "Pandas", "Matplotlib", "Keras"], "answer": "Matplotlib"},
            {"question": "What is cross-validation?", "options": ["Splitting data into training and test sets", "Data normalization", "A model evaluation technique", "Feature extraction"], "answer": "A model evaluation technique"},
            {"question": "Which algorithm is used for clustering?", "options": ["Linear regression", "KNN", "K-means", "Decision trees"], "answer": "K-means"},
            {"question": "Which function is used to load data in Pandas?", "options": ["load()", "read()", "import()", "read_csv()"], "answer": "read_csv()"},
            {"question": "What is overfitting?", "options": ["Model too simple", "Model too complex", "Balanced model", "None of the above"], "answer": "Model too complex"}
        ],

        "Java": [
            {"question": "Which keyword is used to define a class in Java?", "options": ["class", "Class", "define", "struct"], "answer": "class"},
            {"question": "Which of these is a primitive data type in Java?", "options": ["int", "String", "Object", "ArrayList"], "answer": "int"},
            {"question": "Which method is the entry point of any Java program?", "options": ["main()", "start()", "run()", "init()"], "answer": "main()"},
            {"question": "Which of these is not a Java keyword?", "options": ["static", "Boolean", "void", "final"], "answer": "Boolean"},
            {"question": "Which concept allows multiple forms in Java?", "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], "answer": "Polymorphism"},
            {"question": "Which keyword is used to inherit a class in Java?", "options": ["this", "import", "extends", "implements"], "answer": "extends"},
            {"question": "What is the size of `int` in Java?", "options": ["2 bytes", "4 bytes", "8 bytes", "Depends on system"], "answer": "4 bytes"},
            {"question": "Which collection class stores key-value pairs?", "options": ["List", "Set", "Map", "Queue"], "answer": "Map"},
            {"question": "Which exception is thrown when a class is not found?", "options": ["IOException", "NullPointerException", "ClassNotFoundException", "ArithmeticException"], "answer": "ClassNotFoundException"},
            {"question": "Which symbol is used for single-line comments in Java?", "options": ["//", "#", "/*", "--"], "answer": "//"}
        ],

        "Machine Learning": [
            {"question": "What is supervised learning?", "options": ["Learning with labeled data", "Learning without labels", "Clustering", "None"], "answer": "Learning with labeled data"},
            {"question": "Which of these is a supervised algorithm?", "options": ["K-means", "Linear Regression", "PCA", "Apriori"], "answer": "Linear Regression"},
            {"question": "Which algorithm is used for classification tasks?", "options": ["Logistic Regression", "K-means", "PCA", "Apriori"], "answer": "Logistic Regression"},
            {"question": "Which one is a dimensionality reduction technique?", "options": ["PCA", "KNN", "Naive Bayes", "SVM"], "answer": "PCA"},
            {"question": "What is underfitting?", "options": ["Model too complex", "Model too simple", "Perfect fit", "Overtrained model"], "answer": "Model too simple"},
            {"question": "Which library is commonly used in ML with Python?", "options": ["Django", "NumPy", "TensorFlow", "Flask"], "answer": "TensorFlow"},
            {"question": "Which metric is used for regression?", "options": ["Accuracy", "Recall", "MSE", "F1-score"], "answer": "MSE"},
            {"question": "What is the goal of clustering?", "options": ["Predict labels", "Group similar data", "Reduce features", "Evaluate performance"], "answer": "Group similar data"},
            {"question": "Which algorithm works on distance calculation?", "options": ["SVM", "KNN", "Naive Bayes", "Linear Regression"], "answer": "KNN"},
            {"question": "What is the full form of SVM?", "options": ["Support Vector Machine", "Simple Vector Map", "Standard Variable Model", "Support Value Module"], "answer": "Support Vector Machine"}
        ],

        "AI": [
            {"question": "What does AI stand for?", "options": ["Automated Input", "Artificial Intelligence", "Automated Intelligence", "Applied Informatics"], "answer": "Artificial Intelligence"},
            {"question": "Which of these is a branch of AI?", "options": ["Machine Learning", "Robotics", "NLP", "All of the above"], "answer": "All of the above"},
            {"question": "Which algorithm is used in game playing AI?", "options": ["KNN", "Minimax", "Naive Bayes", "SVM"], "answer": "Minimax"},
            {"question": "What is NLP?", "options": ["Natural Learning Processing", "Neural Language Processing", "Natural Language Processing", "Neural Learning Platform"], "answer": "Natural Language Processing"},
            {"question": "Which AI technique is inspired by the brain?", "options": ["Decision Trees", "Neural Networks", "SVM", "KNN"], "answer": "Neural Networks"},
            {"question": "Which language is most commonly used in AI?", "options": ["Python", "Java", "C++", "All of the above"], "answer": "All of the above"},
            {"question": "What is a chatbot an example of?", "options": ["Computer Vision", "Expert System", "NLP application", "Voice recognition"], "answer": "NLP application"},
            {"question": "What is reinforcement learning?", "options": ["Learning with reward", "Unsupervised learning", "Transfer learning", "None"], "answer": "Learning with reward"},
            {"question": "What is an intelligent agent?", "options": ["Robot", "Software", "System that perceives and acts", "None of the above"], "answer": "System that perceives and acts"},
            {"question": "What is the Turing Test used for?", "options": ["Measuring CPU speed", "Testing AI intelligence", "Machine translation", "Speech recognition"], "answer": "Testing AI intelligence"}
        ]
    }

    
  
    
    # Function to calculate the score
    def calculate_score(correct_answers, total_questions):
        score_percentage = (correct_answers / total_questions) * 100
        if score_percentage >= 80:
            return "High"
        elif score_percentage >= 50:
            return "Medium"
        else:
            return "Low"
    
    # Function to provide feedback
    def provide_feedback(performance):
        if performance == "Low":
            return "Hint: Review key concepts like Data Structures, Algorithms, and Basic Syntax."
        elif performance == "Medium":
            return "Good job! Focus on understanding more advanced concepts and practice more."
        else:
            return "Excellent! Keep up the great work and keep exploring advanced topics!"
    
    # Streamlit Webpage Layout
    # st.title("📚 Quiz on Python, Data Science, and More")
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:30px;">{"📚 Assesment Page"}</h1>', unsafe_allow_html=True)

    st.write("Choose a subject and start answering the questions. After submitting, you'll get feedback based on your performance.")
    
    # Subject selection
    subject = st.selectbox("Select a Subject:", subjects)
    
    # Fetch questions based on subject
    questions = questions_data.get(subject, [])
    
    # Initialize session state
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    
    # Display questions and options
    correct_answers = 0
    for i, q in enumerate(questions):
        st.markdown(f"### {i+1}. {q['question']}")
        options = q['options']
        user_answer = st.radio(f"Choose your answer:", options, key=f"question_{i}")
        
        # Check the answer
        if user_answer == q['answer']:
            correct_answers += 1
            st.session_state.answers.append(True)  # Mark answer as correct
        else:
            st.session_state.answers.append(False)  # Mark answer as incorrect
    
    # Submit button to calculate score
    if st.button("Submit Quiz"):
        total_questions = len(questions)
        performance = calculate_score(correct_answers, total_questions)
        feedback = provide_feedback(performance)
    
        # Display score and feedback
        st.markdown(f"### Your Score: {correct_answers}/{total_questions} ({(correct_answers/total_questions)*100}%)")
        st.markdown(f"### Your performance is: {performance}")
        st.markdown(f"### Feedback: {feedback}")
    
        # Display overall results with icons
        st.success("🏆 Well done! Keep practicing to improve your knowledge.")
        st.info("🔍 Review the topics and keep learning!")
    
        # Reset answers for the next quiz
        st.session_state.answers = []
    
                
            
            
if selected=="Study Plan":

     import subprocess
     subprocess.run(['python','-m','streamlit','run','StudyPlan.py'])


            
if selected=="Note Summarization":

     import subprocess
     subprocess.run(['python','-m','streamlit','run','NoteSummarize.py'])



if selected=="Answer Evaluation":

     import subprocess
     subprocess.run(['python','-m','streamlit','run','ans_st.py'])



if selected=="Q&A":

    import streamlit as st
    
    # Initialize session state to store questions and answers
    if 'qa_list' not in st.session_state:
        st.session_state.qa_list = []  # list of dicts with {"question": "", "answer": ""}
    
    # st.title("💬 Community Q&A Board")
    st.markdown("💬 Share your questions, provide answers, and collaborate with others! 🚀")
    
    # --- Question Submission Section ---
    st.markdown("### 📝 **Post a New Question**")
    question_input = st.text_area("❓ Type your question here", key="new_question")
    
    if st.button("➕ Submit Question"):
        if question_input.strip():
            st.session_state.qa_list.append({"question": question_input, "answer": ""})
            st.success("✅ Question posted successfully!")
        else:
            st.warning("⚠️ Please enter a question before submitting.")
    
    # --- Display Questions and Allow Answering ---
    st.markdown("---")
    st.markdown("## 📚 **Questions and Answers**")
    
    if not st.session_state.qa_list:
        st.info("No questions posted yet. Be the first to ask!")
    else:
        for idx, qa in enumerate(st.session_state.qa_list):
            st.markdown(f"---\n### ❓ **Q{idx+1}:** {qa['question']}")
    
            # If answer exists, show it
            if qa["answer"]:
                st.markdown(f"**💡 Answer:**\n> {qa['answer']}")
            else:
                answer = st.text_area("✍️ Your Answer:", key=f"answer_{idx}")
                if st.button("📨 Submit Answer", key=f"submit_{idx}"):
                    if answer.strip():
                        st.session_state.qa_list[idx]["answer"] = answer
                        st.success("✅ Answer submitted!")
                    else:
                        st.warning("⚠️ Please type an answer before submitting.")
    
    # Footer
    st.markdown("---")
    st.markdown("🔁 _Your contributions help others learn. Keep asking, keep answering!_ 🙌")









            
        
        
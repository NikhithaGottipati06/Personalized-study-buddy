# ================ Input Packages =========================

import streamlit as st

import base64
import matplotlib.image as mpimg
import cv2

import matplotlib.pyplot as plt 
from streamlit_option_menu import option_menu
import numpy as np

# ================ Background image ==============================


st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Integration of AI for adaptive learning for MCQ selection "}</h1>', unsafe_allow_html=True)


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
    options=["Exam Score Prediction","Study Plan","Note Summarization","Q&A"],  
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



if selected=="Exam Score Prediction":
    
    
    import pandas as pd

    data_frame=pd.read_csv("exam_performance_dataset.csv")
           
    gra = data_frame['Grades'].unique()
    
    pat = data_frame['Pattern'].unique()
    
    learn = data_frame['Learning Speed'].unique()
    
    
    sub = data_frame['Subjects'].unique()
    
    hab = data_frame['Revision Habits'].unique()
    
    
    import pickle
    import pandas as pd
    
    with open('model.pickle', 'rb') as f:
       rf = pickle.load(f)
       
       
     #1
    q1 = st.number_input("Ener Student ID ") 
    
    q2 = st.number_input("Ener Scores ") 

    
    d3=st.selectbox("Choose Grades",gra)     

    def get_alphabetical_position(gra):
           # Extract the alphabetical part from the SKU
           alphabet_part = ''.join([char for char in gra if char.isalpha()])
           # Calculate the alphabetical position (A=1, B=2, ..., Z=26)
           return sum((ord(char) - ord('A') + 1) for char in alphabet_part)
       
       # Validate the choice
    if d3 in gra:
        # Get the alphabetical position of the chosen SKU
        position = get_alphabetical_position(d3)
        q3=position
        print(f"The alphabetical position of '{d3}' is: {position}")
    else:
        print("Invalid SKU choice.")
        q3=1    
 
    
    d4=st.selectbox("Choose Patterns",pat)     

    def get_alphabetical_position(pat):
           # Extract the alphabetical part from the SKU
           alphabet_part = ''.join([char for char in gra if char.isalpha()])
           # Calculate the alphabetical position (A=1, B=2, ..., Z=26)
           return sum((ord(char) - ord('A') + 1) for char in alphabet_part)
       
       # Validate the choice
    if d4 in pat:
        # Get the alphabetical position of the chosen SKU
        position = get_alphabetical_position(d4)
        q4=position
        print(f"The alphabetical position of '{d4}' is: {position}")
    else:
        print("Invalid SKU choice.")
        q4=1        
    
    
    d5=st.selectbox("Choose Learning Speed",learn)     

    def get_alphabetical_position(learn):
           # Extract the alphabetical part from the SKU
           alphabet_part = ''.join([char for char in gra if char.isalpha()])
           # Calculate the alphabetical position (A=1, B=2, ..., Z=26)
           return sum((ord(char) - ord('A') + 1) for char in alphabet_part)
       
       # Validate the choice
    if d5 in learn:
        # Get the alphabetical position of the chosen SKU
        position = get_alphabetical_position(d5)
        q5=position
        print(f"The alphabetical position of '{d5}' is: {position}")
    else:
        print("Invalid SKU choice.")
        q5=1      
    
    
    
    d6=st.selectbox("Choose Subjects",sub)     

    def get_alphabetical_position(sub):
           # Extract the alphabetical part from the SKU
           alphabet_part = ''.join([char for char in sub if char.isalpha()])
           # Calculate the alphabetical position (A=1, B=2, ..., Z=26)
           return sum((ord(char) - ord('A') + 1) for char in alphabet_part)
       
       # Validate the choice
    if d6 in sub:
        # Get the alphabetical position of the chosen SKU
        position = get_alphabetical_position(d6)
        q6=position
        print(f"The alphabetical position of '{d6}' is: {position}")
    else:
        print("Invalid SKU choice.")
        q6=1         
    
    
    d7=st.selectbox("Choose Revision Habits",hab)     

    def get_alphabetical_position(hab):
           # Extract the alphabetical part from the SKU
           alphabet_part = ''.join([char for char in hab if char.isalpha()])
           # Calculate the alphabetical position (A=1, B=2, ..., Z=26)
           return sum((ord(char) - ord('A') + 1) for char in alphabet_part)
       
       # Validate the choice
    if d7 in hab:
        # Get the alphabetical position of the chosen SKU
        position = get_alphabetical_position(d7)
        q7=position
        print(f"The alphabetical position of '{d6}' is: {position}")
    else:
        print("Invalid SKU choice.")
        q7=1     
    
    
    aa = st.button("PREDICT")
    
    
    if aa:
        
        
            data =[q1,q2,q3,q4,q5,q6,q7]
            data1=np.array(data).reshape(1, -1)
            pred_rf = rf.predict(data1)
            
            
    
            if pred_rf == 0:
                st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:30px;font-family:Caveat, sans-serif;">{"Identified = HIGH "}</h1>', unsafe_allow_html=True)
                    
    











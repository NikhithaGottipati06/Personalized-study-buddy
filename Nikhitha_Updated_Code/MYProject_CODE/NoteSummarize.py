import streamlit as st
from PIL import Image
import easyocr
from transformers import pipeline
import base64

import pandas as pd
import sqlite3
from streamlit_option_menu import option_menu


# ================ Background image ===

st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"📝 Note Summarization"}</h1>', unsafe_allow_html=True)


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
    
add_bg_from_local('st1.jpg')    
    
    
    
import streamlit as st
from transformers import pipeline

# Load the summarization model from Hugging Face
summarizer = pipeline("summarization")

# Function to summarize the input text
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Provide a description of the app
st.markdown("""
    **Welcome to the Note Summarizer!**
    
    This app takes a paragraph of text and summarizes it using NLP techniques.
    Just enter your text in the box below, and let the system summarize it for you!
    """)

# Text input area
input_text = st.text_area("Enter your text below:", height=200)

# If the user provides input
if input_text:
    # Display the original input
    st.subheader("🔍 Original Text:")
    st.write(input_text)
    
    # Summarize the text
    st.subheader("✂️ Summarized Text:")
    summary = summarize_text(input_text)
    st.write(summary)

    # Show a success message
    st.success("✅ Summary generated successfully!")
    
else:
    # Provide a message if no text is input
    st.warning("⚠️ Please enter a paragraph of text to summarize.")
    
# Add a footer message for user interaction
st.markdown("""
    **Note:** 
    - You can input any length of text, and the system will summarize it for you.
    - Try with long articles or any content you want to quickly understand in short form.
""")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# # Load HuggingFace summarizer model
# summarizer = pipeline("summarization")

# # Initialize the EasyOCR Reader
# reader = easyocr.Reader(['en'])  # You can add other languages as needed

# # Function to summarize typed text
# def summarize_text(text):
#     summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
#     return summary[0]['summary_text']

# # Function to extract text from an image using EasyOCR
# def extract_text_from_image(image):
#     result = reader.readtext(image)  # Perform OCR on the image
#     extracted_text = ''
#     for detection in result:
#         extracted_text += detection[1] + ' '  # detection[1] contains the recognized text
#     return extracted_text

# # Streamlit interface
# # st.title("Note Summarizer")
# st.write("""
#     This tool can help you summarize handwritten or typed notes.
#     - If you have handwritten notes, upload an image.
#     - If you have typed notes, you can input them directly.
# """)

# # Option for user to choose input type
# input_type = st.radio("Choose the type of input", ("Handwritten Notes (Image)", "Typed Notes (Text)"))

# if input_type == "Handwritten Notes (Image)":
#     st.subheader("Upload an image of your handwritten notes")
#     uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#     if uploaded_image is not None:
#         image = Image.open(uploaded_image)
#         st.image(image, caption="Uploaded Image", use_column_width=True)
#         st.write("Extracting text from the image...")

#         # Extract text using EasyOCR
#         extracted_text = extract_text_from_image(uploaded_image)
#         st.text_area("Extracted Text", extracted_text, height=200)

#         # Provide summarized output
#         if st.button("Summarize"):
#             if extracted_text.strip():
#                 summary = summarize_text(extracted_text)
#                 st.subheader("Summary:")
#                 st.write(summary)
#             else:
#                 st.warning("No text was extracted from the image.")

# elif input_type == "Typed Notes (Text)":
#     st.subheader("Input your typed notes")
#     typed_notes = st.text_area("Enter your notes here...", height=200)

#     if typed_notes.strip():
#         if st.button("Summarize"):
#             summary = summarize_text(typed_notes)
#             st.subheader("Summary:")
#             st.write(summary)

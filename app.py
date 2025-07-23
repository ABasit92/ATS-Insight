from dotenv import load_dotenv

load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Set your Poppler path here
        poppler_path = r"C:\Program Files (x86)\poppler\Library\bin"  # <-- Update this path to where you extracted Poppler

        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=poppler_path
        )

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Insight", page_icon=":rocket:", layout="centered")

# Custom CSS for a modern blue theme and attractive design
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #0f2027 0%, #2c5364 100%);
        min-height: 100vh;
    }
    
    .blue-header {
        color: #4fd1c5;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 0.2rem;
        text-align: center;
        line-height: 1.1;
        background: linear-gradient(60deg, #e0f7fa 10%, #4fd1c5 50%, #81e6d9 50%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        
        
    }
    .tagline {
        font-size: 1.08rem;
        font-style: italic;
        text-align: center;
        margin-bottom: 2.2rem;
        margin-top: 0.2rem;
        background: linear-gradient(90deg, #e0f7fa 100%, #81e6d9 80%, #4fd1c5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        
        
    }
    .stTextArea textarea {
        background-color: #25475e !important;
        border: 2px solid #4fd1c5 !important;
        color: #fff !important;
        font-size: 1.08rem !important;
        border-radius: 8px !important;
        min-height: 120px !important;
        font-weight: 500 !important;
    }
    .stFileUploader {
        background-color: #25475e !important;
        border-radius: 8px !important;
        border: 2px solid #4fd1c5 !important;
        margin-bottom: 1.5rem !important;
        padding: 0.5rem !important;
    }
    label, .stTextArea label, .stFileUploader label {
        color: #fff !important;
        font-weight: 600 !important;
        font-size: 1.08rem !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #11998e 60%, #38ef7d 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 1.08rem !important;
        margin-right: 0.7rem !important;
        margin-top: 0.5rem !important;
        padding: 0.5rem 1.5rem !important;
        border: none !important;
        box-shadow: 0 2px 8px #18344a;
        transition: background 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #43cea2 60%, #185a9d 100%) !important;
        color: #fff !important;
    }
    .stSubheader {
        color: #4fd1c5 !important;
        font-weight: 700 !important;
        margin-top: 2rem !important;
    }
    .stAlert {
        border-radius: 8px !important;
        font-size: 1.05rem !important;
    }
    /* PDF uploaded success message */
    .stNotification-success {
        background-color: #222 !important;
        color: #fff !important;
        border-radius: 8px !important;
        font-size: 1.08rem !important;
        font-weight: 600 !important;
        border: 1.5px solid #4fd1c5 !important;
    }
    /* Uploaded PDF file name */
    .stFileUploader .uploadedFileName {
        color: #111 !important;
        font-size: 1.08rem !important;
        font-weight: 600 !important;
    }
    /* Make sure the file name is visible and styled */
    .stFileUploader .css-1aehpvj, .stFileUploader .css-1c7y2kd {
        color: #111 !important;
        font-size: 1.08rem !important;
        font-weight: 600 !important;
    }
    .button-row {
        display: flex;
        gap: 1.2rem;
        justify-content: center;
        margin-bottom: 1.5rem;
        margin-top: 0.5rem;
        flex-wrap: wrap;
    }
    .button-row form {
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-card'>", unsafe_allow_html=True)
st.markdown("<div class='blue-header'>AI-Powered ATS Resume Optimization Tool</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Instantly analyze, score, and improve your resume for better job matches.</div>", unsafe_allow_html=True)

# Job Description label 
st.markdown("<label style='color:#0a2540;font-weight:600;font-size:1.08rem; margin-top:2rem; margin-bottom:-2.5rem; display:block;'>Job Description:</label>", unsafe_allow_html=True)
input_text = st.text_area("", key="input")

st.markdown("<label style='color:#0a2540;font-weight:600;font-size:1.08rem; margin-top:1.2rem; display:block;'>Upload your resume (PDF):</label>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file is not None:
    st.markdown(
        """
        <div style='background-color:#222; color:#fff; border-radius:8px; padding:0.6rem 1.2rem; display:inline-flex; align-items:center; font-size:1.08rem; font-weight:600; margin-bottom:1rem;'>
            <span style='font-size:1.3rem; margin-right:0.5rem;'>✅</span> PDF Uploaded Successfully
        </div>
        """,
        unsafe_allow_html=True
    )

with st.form("action_buttons", clear_on_submit=False):
    st.markdown(
        """
        <style>
        /* Hide the form box by making it fully transparent and removing border */
        div[data-testid="stForm"] {
            background: transparent !important;
            box-shadow: none !important;
            border: none !important;
            opacity: 0;
            height: 0px;
            min-height: 0px;
            padding: 0 !important;
            margin: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    action = st.form_submit_button("")

input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
You are a career coach and technical recruiter. Based on the provided resume and job description, suggest specific skills, certifications, or experiences the candidate should acquire or improve to increase their chances of landing this job. Be detailed and actionable.
"""

input_prompt4 = """
You are an ATS (Applicant Tracking System) expert. Compare the provided resume and job description, and list the most important keywords, skills, or phrases from the job description that are missing in the resume. Present the missing keywords in a bullet list.
"""

if action:
    selected = st.experimental_get_query_params().get("action", [None])[0]

    import streamlit as st
    import streamlit.components.v1 as components

   

st.markdown(
    """
    <style>
    .stButton {
        display: inline-block !important;
        margin-right: 1.2rem !important;
        margin-bottom: 0.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

button_labels = ["Tell Me About the Resume", "Percentage Match", "How Can I Improvise My Skills?", "What Keywords Are Missing?"]
button_keys = ["about", "match", "improve", "keywords"]

button_width = "250px"  

button_clicked = None
for label, key in zip(button_labels, button_keys):
    if st.button(label, key=key):
        button_clicked = key

st.markdown(
    f"""
    <style>
    .stButton > button {{
        width: {button_width} !important;
        min-width: {button_width} !important;
        max-width: {button_width} !important;
        margin-bottom: 0.5rem !important;
        display: block !important;
        margin-left: 0 !important;
        margin-right: auto !important;
        text-align: left !important;
        padding-left: 1.2rem !important;
        font-size: 1rem !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if button_clicked == "about":
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.markdown(
            """
            <div style='background-color:#222; color:#fff; border-radius:8px; padding:0.6rem 1.2rem; display:inline-flex; align-items:center; font-size:1.08rem; font-weight:600; margin-bottom:1rem;'>
                <span style='font-size:1.3rem; margin-right:0.5rem;'>⚠️</span> Please upload the resume
            </div>
            """,
            unsafe_allow_html=True
        )

elif button_clicked == "match":
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.markdown(
            """
            <div style='background-color:#222; color:#fff; border-radius:8px; padding:0.6rem 1.2rem; display:inline-flex; align-items:center; font-size:1.08rem; font-weight:600; margin-bottom:1rem;'>
                <span style='font-size:1.3rem; margin-right:0.5rem;'>⚠️</span> Please upload the resume
            </div>
            """,
            unsafe_allow_html=True
        )

elif button_clicked == "improve":
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Skill Improvement Suggestions")
        st.write(response)
    else:
        st.markdown(
            """
            <div style='background-color:#222; color:#fff; border-radius:8px; padding:0.6rem 1.2rem; display:inline-flex; align-items:center; font-size:1.08rem; font-weight:600; margin-bottom:1rem;'>
                <span style='font-size:1.3rem; margin-right:0.5rem;'>⚠️</span> Please upload the resume
            </div>
            """,
            unsafe_allow_html=True
        )

elif button_clicked == "keywords":
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("Missing Keywords")
        st.write(response)
    else:
        st.markdown(
            """
            <div style='background-color:#222; color:#fff; border-radius:8px; padding:0.6rem 1.2rem; display:inline-flex; align-items:center; font-size:1.08rem; font-weight:600; margin-bottom:1rem;'>
                <span style='font-size:1.3rem; margin-right:0.5rem;'>⚠️</span> Please upload the resume
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)


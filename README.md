# ATS Insight — AI-Powered Resume Optimization Tool

**ATS Insight** is a modern, visually appealing Streamlit web app that leverages **Google Gemini AI** to analyze resumes against job descriptions. It provides instant feedback tailored to boost job seekers' chances of landing interviews.

✨ Whether you're a job seeker aiming for your dream role or a career coach optimizing resumes, ATS Insight offers **smart, clear, and actionable insights**.

---

## 🧠 What Can It Do?

After uploading a resume and pasting a job description, you can choose from **four intelligent analysis options**:

### 🎯 Features:

- 📄 Upload Resume (PDF)
- 📋 Paste or Upload Job Description
- 📊 AI-Based Resume Analysis
  - Percentage match with JD
  - Keyword and skill extraction
  - Missing skills & suggestions
- 🧠 Uses Gemini API (Google AI)
- 📎 PDF text extraction using Poppler
- 🐍 Built with Python (Anaconda environment)

| Option | Description |
|--------|-------------|
| 🧾 **Tell Me About the Resume** | Professional review highlighting strengths and weaknesses based on the JD |
| 📊 **Percentage Match** | AI-powered matching percentage, missing keywords, and final thoughts |
| 📈 **How Can I Improvise My Skills?** | Personalized skill/certification suggestions to improve the resume |
| 🧩 **What Keywords Are Missing?** | ATS-style scan to detect missing phrases/keywords from the JD |

---

## 🖼️ Interface Preview

> Modern UI built with custom CSS in Streamlit  
> Upload section + custom buttons with smooth layout

![Image](https://github.com/user-attachments/assets/ab19a8dd-3d8a-4c1a-a07c-ff4864e0f45b)
![Image](https://github.com/user-attachments/assets/43cf2878-70a4-4d8c-9b6e-d285f039213a)
![Image](https://github.com/user-attachments/assets/7600b6e7-eb5f-475b-bdc1-9b29bcec6b85)
![Image](https://github.com/user-attachments/assets/7207b30c-10c2-4b29-96d1-2cddcaa86418)
![Image](https://github.com/user-attachments/assets/60559244-adbb-48f3-9bed-de6577dc6aa8)
![Image](https://github.com/user-attachments/assets/f3eb252b-0221-445a-be29-98810f6aed3c)
![Image](https://github.com/user-attachments/assets/208f4bd0-a787-405b-8b8f-6ce0d3f0d77b)
![Image](https://github.com/user-attachments/assets/8517cbd8-8e5a-40b0-aabd-50a9becd3897)
![Image](https://github.com/user-attachments/assets/b1026888-3c74-4453-92a2-bfafa2d7e91c)
![Image](https://github.com/user-attachments/assets/06681987-787a-4b08-838d-5aacdc940398)
![Image](https://github.com/user-attachments/assets/5707f577-6455-49ed-8be5-6f3fc118508c)

---

## 🛠 Tech Stack

- **Streamlit** – Fast Python web apps
- **Google Gemini (via `google-generativeai`)** – LLM-based resume analysis
- **Poppler + `pdf2image`** – Convert PDF to image for Gemini processing
- **Custom CSS** – Beautiful, dark-themed UI for great user experience

# AI-NoteTaker


AI Notetaker is a smart assistant that generates multi-format summaries from meeting transcripts, documents, or voice notes. It helps professionals, students, and researchers quickly capture the essence of lengthy text and transform it into actionable insights.


---

# Features

Generates concise bullet point summaries

Converts notes into structured email drafts

Extracts actionable to-do lists

Supports voice recording and transcription

Works with PDF, TXT, and DOCX uploads

Option to paste text directly

Built-in support for OpenAI GPT and HuggingFace Transformers



---

# Use Cases

Professionals: Summarize meetings and extract action items

Students: Summarize lectures, notes, and study material

Researchers: Compress long papers into digestible insights

Teams: Align tasks and decisions quickly



---

# Tech Stack

Frontend: Streamlit

NLP Models: OpenAI GPT, HuggingFace Transformers (DistilBART)

Speech-to-Text: Whisper

Language: Python

Environment: dotenv for API keys



---

# Project Structure

AI-Notetaker/
│
├── app.py                  # Main Streamlit application
├── src/
│   ├── utils/
│   │   ├── readers.py       # File reading and trimming utilities
│   ├── summarizers/
│   │   ├── gpt.py           # GPT-based summarization logic
│   ├── whisper_utils.py     # Whisper transcription functions
│
├── requirements.txt         # Dependencies
├── .env                     # API keys (not committed)
└── README.md                # Project documentation


---

# Installation

1. Clone the repository:

git clone https://github.com/your-username/ai-notetaker.git
cd ai-notetaker


2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3. Install dependencies:

pip install -r requirements.txt


4. Create a .env file and add your API key:

OPENAI_API_KEY=your_api_key_here
DEFAULT_SUMMARIZER=gpt




---

# Usage

Run the app locally:

streamlit run app.py

Steps:

1. Upload a PDF, TXT, or DOCX file, paste text, or record a voice note.


2. Choose summarizer engine (GPT or HuggingFace).


3. Click "Generate Summaries".


4. Copy results from Bullet Points, Email Draft, or To-Do tabs.




---

# Deployment (HTTPS with Streamlit Cloud)

1. Push your project to GitHub.


2. Go to Streamlit Cloud and connect your GitHub repository.


3. Deploy by selecting your repo and app.py as the entry point.


4. Add your API key as a secret in Streamlit Cloud’s settings.


5. Your app will be live with HTTPS provided automatically.




---

# Skills & Technologies Used

Python (core programming language)

Streamlit (frontend and web app framework)

PyPDF2 / python-docx (document text extraction)

OpenAI GPT API (text summarization with creativity control)

Hugging Face Transformers (fallback summarizer using DistilBART)

Whisper (speech-to-text transcription)

dotenv (environment variable management)

HTML/CSS inside Streamlit (UI polish, background image, styling)

Git & GitHub (version control, deployment integration)


# Outputs Screenshots


1. ![alt text](<Screenshot 2025-08-26 184837.png>) 


2. ![alt text](<Screenshot 2025-08-26 162446.png>) 


3. ![alt text](<Screenshot 2025-08-26 183846.png>) 


4. ![alt text](<Screenshot 2025-08-26 183907.png>) 


5. ![alt text](<Screenshot 2025-08-26 184145.png>) 
 

6. ![alt text](<Screenshot 2025-08-26 184310.png>) 


7. ![alt text](<Screenshot 2025-08-26 184342.png>) 


8. ![alt text](<Screenshot 2025-08-26 184444.png>) 


9. ![alt text](<Screenshot 2025-08-26 184816.png>)





---
# Access AI-NoteTaker


https://ai-notetaker-kipr5yeld8msha5p7nhqqk.streamlit.app/




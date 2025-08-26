import os
import streamlit as st
from dotenv import load_dotenv
from src.utils.readers import read_text_bytes, trim_if_needed
import streamlit.components.v1 as components
# Hugging Face summarizer
from transformers import pipeline
# Whisper transcription
from src.whisper_utils import record_and_transcribe

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")
DEFAULT = os.getenv("DEFAULT_SUMMARIZER", "gpt")

st.set_page_config(page_title="Multi-Format Summarizer", layout="wide")
st.title("AI Meeting & Document Summarizer")

# Controls
summarizer_choice = st.selectbox(
    "Summarizer engine",
    ["gpt", "hf"],
    index=0 if DEFAULT == "gpt" else 1
)
temperature = st.slider(
    "Creativity (lower = factual)",
    0.0, 1.0, 0.2, 0.1,
    help="Only affects GPT path today"
)

uploaded = st.file_uploader(
    "Upload transcript or document (.txt, .pdf, .docx)",
    type=["txt", "pdf", "docx"]
)
raw_text = st.text_area(
    " paste text here",
    height=180,
    placeholder="Paste meeting notes / research text"
)

st.markdown(
    "<p style='font-size:16px; font-weight:600;'>...or paste here Record and transcribe voice note</p>",
    unsafe_allow_html=True
)

transcribed_text = record_and_transcribe()
if transcribed_text:
    raw_text = transcribed_text


col_run, col_clear = st.columns([1, 1])
with col_run:
    run = st.button("Generate Summaries", type="primary")
with col_clear:
    if st.button("Clear"):
        st.experimental_rerun()


# ---------- Helper for chunking large docs ----------
def chunk_text(text, max_words=800):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i + max_words])


# ---------- Helper for copy buttons ----------
def copy_button(label, text_to_copy, key):
    # Escape quotes for JavaScript
    safe_text = text_to_copy.replace('"', '\\"').replace('\n', '\\n')
    component_code = f"""
    <script>
    function copyToClipboard_{key}() {{
        navigator.clipboard.writeText("{safe_text}");
        alert("{label} copied to clipboard!");
    }}
    </script>
    <button onclick="copyToClipboard_{key}()" 
    style="padding:6px 12px; 
    border:none; background:#4CAF50; 
    color:white; border-radius:6px; cursor:pointer; margin-top:8px;">
        Copy {label}
    </button>
    """
    components.html(component_code, height=40)


# ---------- Main Run ----------
if run:
    if not uploaded and not raw_text.strip():
        st.warning("Please upload a file, paste text, or record voice.")
        st.stop()

    if uploaded:
        content = read_text_bytes(uploaded.name, uploaded.read(), uploaded.type)
    else:
        content = raw_text

    content = trim_if_needed(content)
    if len(content.strip()) < 40:
        st.warning("Input looks too short; add more context for better results.")

    with st.spinner("Summarizing..."):
        if summarizer_choice == "gpt":
            from src.summarizers import gpt as engine
            try:
                outputs = engine.summarize_all(content)
            except Exception as e:
                st.error(f"Summarization failed: {e}")
                st.stop()
        else:
            summarizer = pipeline(
                "summarization",
                model="sshleifer/distilbart-cnn-12-6"
            )
            try:
                summaries = []
                for chunk in chunk_text(content):
                    out = summarizer(
                        chunk,
                        max_length=130,
                        min_length=30,
                        do_sample=False
                    )[0]["summary_text"]
                    summaries.append(out)

                final_summary = " ".join(summaries)

                outputs = {
                    "bullets": "- " + final_summary.replace(". ", ".\n- "),
                    "email": f"Hi team,\n\n{final_summary}\n\nBest regards,\n",
                    "todo": "- [ ] " + final_summary.replace(". ", ".\n- [ ] "),
                }
            except Exception as e:
                st.error(f"Summarization failed: {e}")
                st.stop()

    # ---------- Display Results ----------
    st.subheader("Results")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### Bullet Points")
        st.markdown(outputs["bullets"])
        copy_button("Bullets", outputs["bullets"], key="bullets")

    with c2:
        st.markdown("### Email Draft")
        st.text_area("email", value=outputs["email"], height=200)
        copy_button("Email", outputs["email"], key="email")

    with c3:
        st.markdown("### To-Do / Actions")
        st.markdown(outputs["todo"])
        copy_button("To-Do", outputs["todo"], key="todo")

    st.divider()
    st.caption("Tip: You can upload files, paste text, or record your voice to generate summaries.")


# ---------- Sidebar ----------
st.sidebar.header("About")
st.sidebar.write("Multi-format summaries in one click: bullets, email, to-do.")
st.sidebar.write("Engines: OpenAI GPT (primary) or Hugging Face (fallback).")

from transformers import pipeline
import streamlit as st
import tempfile

# Load Whisper model locally (first time it will download from Hugging Face Hub)
transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small"   # you can also try "openai/whisper-base" (faster) or "openai/whisper-medium" (better accuracy)
)

def record_and_transcribe():
    """
    Streamlit function to upload audio file and transcribe using local Whisper model.
    """
    st.subheader(" Upload Voice Note to Get Summary")

    # File uploader
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "mp4"])

    if audio_file:
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            tmpfile.write(audio_file.getbuffer())
            tmp_path = tmpfile.name

        # Run transcription
        result = transcriber(tmp_path)

        # Show transcription
        st.write(" Transcribed Text:")
        st.success(result["text"])

        return result["text"]

    return None

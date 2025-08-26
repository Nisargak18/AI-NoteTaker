from transformers import pipeline
import streamlit as st
import tempfile
from pydub import AudioSegment
import math
import os

# Load Whisper model
transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small"
)

def record_and_transcribe(chunk_length_sec=30):
    """
    Streamlit function to upload audio file and transcribe using Whisper.
    Handles long audio by splitting into smaller chunks (default 30s each).
    """
    st.subheader("Upload Voice Note to Get Summary")

    # File uploader
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "mp4"])

    if audio_file:
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            tmpfile.write(audio_file.getbuffer())
            tmp_path = tmpfile.name

        # Load audio with pydub
        audio = AudioSegment.from_file(tmp_path)
        duration_sec = len(audio) / 1000
        st.info(f"Audio duration: {duration_sec:.2f} seconds")

        # Split into chunks
        num_chunks = math.ceil(duration_sec / chunk_length_sec)
        transcribed_text = ""

        for i in range(num_chunks):
            start_ms = i * chunk_length_sec * 1000
            end_ms = min((i + 1) * chunk_length_sec * 1000, len(audio))
            chunk = audio[start_ms:end_ms]

            # Save chunk to temp file
            chunk_file = f"{tmp_path}_chunk{i}.wav"
            chunk.export(chunk_file, format="wav")

            # Transcribe chunk
            result = transcriber(chunk_file, return_timestamps=False)
            transcribed_text += result["text"] + " "

            # Delete chunk file
            os.remove(chunk_file)

        # Show transcription
        st.write("Transcribed Text:")
        st.success(transcribed_text.strip())

        return transcribed_text.strip()

    return None

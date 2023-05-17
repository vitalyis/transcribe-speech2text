import streamlit as st
import os
from pydub import AudioSegment
from google.cloud import speech

# Set up Google Cloud credentials (replace 'path_to_service_account_key.json' with your own key file)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "loyal-surfer-333701-b1b753aa1fde.json"

# Create a client for the Google Cloud Speech-to-Text API
client = speech.SpeechClient()

# Function to convert audio file to MP3 format
def convert_to_mp3(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="mp3")

# Function to transcribe speech from audio file
def transcribe_speech(audio_file, accent):
    with st.spinner("Transcribing speech..."):
        # Convert audio file to MP3 format
        mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
        convert_to_mp3(audio_file, mp3_file)

        # Load MP3 audio file
        with open(mp3_file, "rb") as file:
            content = file.read()

        # Configure speech recognition request
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code="en-IN",
        )

        # Specify accent hint if provided
        if accent:
            config.speech_contexts[0].phrases.append(accent)

        # Perform speech recognition
        response = client.recognize(config=config, audio=audio)

        # Extract and return transcriptions
        transcriptions = [result.alternatives[0].transcript for result in response.results]
        return "\n".join(transcriptions)

# Streamlit app
def main():
    st.title("Speech-to-Text Transcription")
    st.write("Upload an audio file to transcribe.")

    # File upload
    audio_file = st.file_uploader("Upload Audio File", type=["m4a"])

    # Accent selection
    accent = st.text_input("Accent (Optional)")

    # Transcription button
    if st.button("Transcribe"):
        if audio_file is not None:
            # Save the uploaded file temporarily
            temp_file = os.path.join(".", audio_file.name)
            with open(temp_file, "wb") as file:
                file.write(audio_file.getbuffer())
            # Perform transcription
            transcription = transcribe_speech(temp_file, accent)
            # Display the transcription
            st.success("Transcription:")
            st.write(transcription)
            # Delete the temporary files
            os.remove(temp_file)
            os.remove(mp3_file)
        else:
            st.error("Please upload an audio file.")

if __name__ == "__main__":
    main()

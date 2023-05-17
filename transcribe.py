import streamlit as st
from google.cloud import speech_v1p1beta1 as speech
import os
import audioread

# ... Your other code ...

# Function to transcribe speech from audio file
def transcribe_speech(audio_file, accent):
    with st.spinner("Transcribing speech..."):
        # Convert M4A to WAV if needed
        if audio_file.endswith(".m4a"):
            wav_file = audio_file[:-4] + ".wav"
            with audioread.audio_open(audio_file) as src:
                with audioread.audio_write(wav_file, src.channels, src.samplerate, "wav") as dst:
                    for buf in src:
                        dst.write(buf)
            audio_file = wav_file

        # Load audio file
        with open(audio_file, "rb") as file:
            content = file.read()

        # Configure speech recognition request
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-IN",
            use_enhanced=True,
            model="video",
            metadata={"interaction_type": "DISCUSSION"},
            diarization_config=speech.SpeakerDiarizationConfig(
                enable_speaker_diarization=True,
                min_speaker_count=2,
                max_speaker_count=6,
            ),
        )

        # Specify accent hint if provided
        if accent:
            config.speech_contexts[0].phrases.append(accent)

        # Perform speech recognition
        response = client.recognize(config=config, audio=audio)

        # Extract and return transcriptions
        transcriptions = [result.alternatives[0].transcript for result in response.results]
        return "\n".join(transcriptions)

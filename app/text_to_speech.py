import pyttsx3
from io import BytesIO
import os

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def generate_audio_file(text):
    """Generates an audio file from English text and returns it as a BytesIO object."""
    audio = BytesIO()
    try:
        engine.save_to_file(text, "output.mp3")
        engine.runAndWait()
        with open("output.mp3", "rb") as file:
            audio.write(file.read())
        os.remove("output.mp3")  # Cleanup
        audio.seek(0)  # Reset BytesIO pointer
    except Exception as e:
        raise RuntimeError(f"Text-to-Speech Error: {str(e)}")
    return audio

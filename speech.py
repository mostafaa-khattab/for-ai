import os

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

import tempfile
import speech_recognition as sr
from pydub import AudioSegment


AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"


def speech_to_text(audio_bytes):

    recognizer = sr.Recognizer()

    webm_path = None
    wav_path = None

    try:

        webm_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".webm"
        )

        webm_file.write(audio_bytes)
        webm_file.close()

        webm_path = webm_file.name


        wav_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        wav_file.close()

        wav_path = wav_file.name


        audio = AudioSegment.from_file(
                webm_path,
                format="webm",
                codec="opus"
        )


        audio.export(
            wav_path,
            format="wav"
        )


        with sr.AudioFile(wav_path) as source:

            audio_data = recognizer.record(source)


        text = recognizer.recognize_google(
            audio_data,
            language="ar-EG"
        )

        return text


    except Exception as e:

        print("ERROR:", e)

        return None


    finally:

        if webm_path and os.path.exists(webm_path):
            os.remove(webm_path)

        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)
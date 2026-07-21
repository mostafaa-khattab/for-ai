import asyncio
import edge_tts

from config import VOICE_NAME


async def save_audio(text, filename="assets/response.mp3"):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE_NAME
    )

    await communicate.save(filename)

    return filename


def text_to_speech(text):

    return asyncio.run(
        save_audio(text)
    )
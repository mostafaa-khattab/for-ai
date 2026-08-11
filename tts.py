```python
import asyncio
import edge_tts
import os

from config import VOICE_NAME


async def save_audio(text, filename="assets/response.mp3"):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE_NAME
        )

        await communicate.save(filename)

        if not os.path.exists(filename):
            raise Exception("Audio file was not created.")

        if os.path.getsize(filename) == 0:
            raise Exception("Audio file is empty.")

        return filename

    except Exception as e:
        print(f"TTS Error: {e}")
        raise


def text_to_speech(text):
    return asyncio.run(save_audio(text))
```

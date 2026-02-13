import os
from pydub import AudioSegment
from config.settings import AUDIO_DIR, CLIP_DIR
from src.utils import setup_logger

logger = setup_logger()


def cut_audios(duration):

    os.makedirs(CLIP_DIR, exist_ok=True)

    count = 0

    for file in os.listdir(AUDIO_DIR):

        if not file.lower().endswith((".mp3", ".wav", ".m4a")):
            continue

        input_path = os.path.join(AUDIO_DIR, file)

        try:

            audio = AudioSegment.from_file(input_path)

            clip = audio[:duration * 1000]

            output_path = os.path.join(CLIP_DIR, f"clip_{count}.mp3")

            clip.export(output_path, format="mp3")

            logger.info(f"Processed: {file}")

            count += 1

        except Exception as e:

            logger.warning(f"Skipping corrupted file: {file}")
            continue

    if count == 0:
        raise Exception("No valid audio files found")

    logger.info(f"{count} clips created successfully")

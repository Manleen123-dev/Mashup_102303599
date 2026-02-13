import os
import logging
from pydub import AudioSegment

logger = logging.getLogger(__name__)


def convert_to_mp3():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    videos_dir = os.path.join(base_dir, "data", "videos")
    audios_dir = os.path.join(base_dir, "data", "audios")

    os.makedirs(audios_dir, exist_ok=True)

    files = os.listdir(videos_dir)

    for file in files:

        video_path = os.path.join(videos_dir, file)

        # skip non-video files
        if not os.path.isfile(video_path):
            continue

        try:

            filename = os.path.splitext(file)[0]
            audio_path = os.path.join(audios_dir, filename + ".mp3")

            logger.info(f"Converting: {file}")

            audio = AudioSegment.from_file(video_path)
            audio.export(audio_path, format="mp3")

            logger.info(f"Saved: {audio_path}")

        except Exception as e:

            logger.warning(f"Skipping corrupted file: {file}")
            logger.warning(str(e))


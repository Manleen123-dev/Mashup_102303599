import os
import logging
from pydub import AudioSegment

logger = logging.getLogger(__name__)


def merge_clips(output_filename):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    clips_dir = os.path.join(base_dir, "data", "clips")
    output_dir = os.path.join(base_dir, "data", "output")

    os.makedirs(output_dir, exist_ok=True)

    final_audio = AudioSegment.empty()

    files = sorted(os.listdir(clips_dir))

    if len(files) == 0:
        raise Exception("No clips found to merge")

    for file in files:

        clip_path = os.path.join(clips_dir, file)

        try:

            logger.info(f"Merging: {file}")

            audio = AudioSegment.from_mp3(clip_path)

            final_audio += audio

        except Exception as e:

            logger.warning(f"Skipping corrupted clip: {file}")
            logger.warning(str(e))

    output_path = os.path.join(output_dir, output_filename)

    final_audio.export(output_path, format="mp3")

    logger.info(f"Mashup saved at: {output_path}")

    return output_path

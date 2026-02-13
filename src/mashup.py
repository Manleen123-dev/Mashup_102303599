import os
import logging

from src.downloader import download_videos
from src.converter import convert_to_mp3
from src.cutter import cut_audios
from src.merger import merge_clips
from src.utils import create_zip


# logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def create_mashup(singer, count, duration, output_filename):
    """
    Complete mashup pipeline

    Steps:
    1. Download videos
    2. Convert to mp3
    3. Cut clips
    4. Merge clips
    5. Create ZIP
    """

    try:

        logger.info("Starting Mashup Creation...")
        logger.info(f"Singer: {singer}")
        logger.info(f"Videos: {count}")
        logger.info(f"Duration per clip: {duration}")

        # folders
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        videos_dir = os.path.join(base_dir, "data", "videos")
        audios_dir = os.path.join(base_dir, "data", "audios")
        clips_dir = os.path.join(base_dir, "data", "clips")
        output_dir = os.path.join(base_dir, "data", "output")

        # ensure folders exist
        os.makedirs(videos_dir, exist_ok=True)
        os.makedirs(audios_dir, exist_ok=True)
        os.makedirs(clips_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # output path
        output_mp3 = os.path.join(output_dir, output_filename)

        logger.info("Step 1: Downloading videos...")
        download_videos(singer, count)

        logger.info("Step 2: Converting videos to MP3...")
        convert_to_mp3()

        logger.info("Step 3: Cutting audio clips...")
        cut_audios(duration)

        logger.info("Step 4: Merging clips...")
        merge_clips(output_mp3)

        logger.info(f"Mashup created: {output_mp3}")

        logger.info("Step 5: Creating ZIP...")
        zip_path = create_zip(output_mp3)

        logger.info(f"ZIP created: {zip_path}")

        logger.info("Mashup creation completed successfully.")

        return zip_path

    except Exception as e:

        logger.error(f"Error in mashup creation: {str(e)}")
        raise



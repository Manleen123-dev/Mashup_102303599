import yt_dlp
import os
from config.settings import AUDIO_DIR
from src.utils import setup_logger

logger = setup_logger()

def download_videos(singer, count):

    try:

        logger.info(f"Downloading {count} songs")

        os.makedirs(AUDIO_DIR, exist_ok=True)

        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{AUDIO_DIR}/%(title)s.%(ext)s',
            'quiet': False,
            'noplaylist': False,

            # THIS IS CRITICAL
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        query = f"ytsearch{count}:{singer}"

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([query])

        logger.info("Download completed")

    except Exception as e:
        logger.error(str(e))
        raise



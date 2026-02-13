import logging
from config.settings import LOG_FILE

def setup_logger():

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()
import zipfile
import os

def create_zip(mp3_path):
    
    zip_path = mp3_path.replace(".mp3", ".zip")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(mp3_path, os.path.basename(mp3_path))

    return zip_path

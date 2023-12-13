import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve()
load_dotenv()

BOT_TOKEN = os.environ.get("BOT TOKEN")

ADMIN_Azizbek = os.environ.get("ADMIN_AZIZBEK")
ADMIN_LIST = os.environ.get("ADMIN_LIST").split(',')

import json
import os
import shutil
from datetime import datetime

from config import DATABASE_FILE

DEFAULT_DATABASE = {
    "users": {},
    "stats": {
        "total_users": 0,
        "total_downloads": 0,
        "today_downloads": 0,
        "today_users": 0,
        "errors": 0,
        "blocked_users": 0
    },
    "platforms": {
        "youtube": 0,
        "tiktok": 0,
        "instagram": 0,
        "facebook": 0,
        "twitter": 0,
        "threads": 0,
        "reddit": 0,
        "pinterest": 0,
        "vimeo": 0
    },
    "downloads": [],
    "blocked": [],
    "logs": [],
    "last_reset": datetime.now().strftime("%Y-%m-%d")
}


def init_db():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_DATABASE, f, indent=4, ensure_ascii=False)


def load_db():
    init_db()

    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    with open(DATABASE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def backup():
    if os.path.exists(DATABASE_FILE):
        shutil.copy(
            DATABASE_FILE,
            DATABASE_FILE + ".bak"
      )

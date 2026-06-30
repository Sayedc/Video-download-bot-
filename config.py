import os

# ===============================
# BOT
# ===============================

BOT_NAME = "Alhawy Downloader"
BOT_VERSION = "3.0.0"

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ===============================
# ADMINS
# ===============================

ADMIN_IDS = [
    int(x)
    for x in os.getenv("ADMIN_IDS", "").split(",")
    if x.strip()
]

# ===============================
# PATHS
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOWNLOADS_PATH = os.path.join(BASE_DIR, "downloads")

COOKIES_FILE = os.path.join(BASE_DIR, "cookies.txt")

LOGS_PATH = os.path.join(BASE_DIR, "logs")

DATABASE_FILE = os.path.join(BASE_DIR, "database.json")

# ===============================
# SIGNATURE
# ===============================

SIGNATURE = "✨ Powered By Alhawy"

# ===============================
# DOWNLOAD
# ===============================

MAX_CONCURRENT_DOWNLOADS = 5

MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024

DEFAULT_VIDEO_QUALITY = "720"

ALLOW_AUDIO = True

ALLOW_VIDEO = True

DELETE_FILES_AFTER_SEND = True

DOWNLOAD_TIMEOUT = 600

# ===============================
# SECURITY
# ===============================

MAX_REQUESTS_PER_MINUTE = 10

AUTO_BLOCK = True

BLOCK_AFTER_FAILED = 10

# ===============================
# CACHE
# ===============================

ENABLE_CACHE = True

CACHE_TIME = 3600

# ===============================
# DEBUG
# ===============================

DEBUG = False

# ===============================
# STICKERS
# ===============================

SUCCESS_STICKERS = [
    "🎉",
    "🔥",
    "🚀",
    "⚡",
    "✅"
]

ERROR_STICKERS = [
    "❌",
    "⚠️",
    "💥",
    "🚫"
]

PROCESSING_STICKERS = [
    "⏳",
    "📥",
    "⚙️",
    "🚀"
]

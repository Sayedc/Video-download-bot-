import os

# ==========================
# Telegram
# ==========================
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# حط الآيدي بتاعك هنا
ADMIN_IDS = [
    5671168695
]

# ==========================
# Bot
# ==========================
BOT_NAME = "Alhawy Downloader"

SIGNATURE = "✨ 𝓐𝓵𝓱𝓪𝔀𝔂 ✨"

VERSION = "3.0"

# ==========================
# Download
# ==========================
DOWNLOADS_PATH = "downloads"

MAX_CONCURRENT_DOWNLOADS = 3

MAX_FILE_SIZE = 1024 * 1024 * 1024  # 1GB

# ==========================
# Security
# ==========================
RATE_LIMIT = 10
RATE_LIMIT_WINDOW = 60

AUTO_DELETE_FILES = True

# ==========================
# Database
# ==========================
DATABASE_FILE = "database/database.json"

# ==========================
# Cookies
# ==========================
COOKIES_FILE = "cookies.txt"

# ==========================
# Logs
# ==========================
LOGS_FOLDER = "logs"

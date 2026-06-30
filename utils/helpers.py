import re
import random
import yt_dlp

# ==========================
# استخراج الرابط
# ==========================

def extract_link(text: str):
    pattern = r"https?://[^\s]+"
    match = re.search(pattern, text)
    return match.group(0) if match else None


# ==========================
# تحديد المنصة
# ==========================

def get_platform(url: str):
    url = url.lower()

    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"

    if "tiktok.com" in url:
        return "tiktok"

    if "instagram.com" in url:
        return "instagram"

    if "facebook.com" in url or "fb.watch" in url:
        return "facebook"

    if "twitter.com" in url or "x.com" in url:
        return "twitter"

    if "threads.net" in url:
        return "threads"

    return "unknown"


# ==========================
# التحقق من الرابط
# ==========================

def is_valid_url(url):
    return extract_link(url) is not None


# ==========================
# معلومات الفيديو
# ==========================

def get_video_info(url):

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            return {
                "title": info.get("title", "Unknown"),
                "duration": info.get("duration", 0),
                "uploader": info.get("uploader", "Unknown"),
                "thumbnail": info.get("thumbnail"),
                "webpage_url": info.get("webpage_url"),
                "extractor": info.get("extractor"),
                "view_count": info.get("view_count", 0)
            }

    except Exception:
        return None


# ==========================
# تحويل الحجم
# ==========================

def format_size(size):

    if not size:
        return "Unknown"

    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} TB"


# ==========================
# تحويل الوقت
# ==========================

def format_duration(seconds):

    if not seconds:
        return "0:00"

    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60

    if h:
        return f"{h}:{m:02}:{s:02}"

    return f"{m}:{s:02}"


# ==========================
# رسائل
# ==========================

PROCESSING_MESSAGES = [
    "⏳ جاري التحميل...",
    "📥 جاري تجهيز الملف...",
    "⚡ لحظات...",
    "🚀 جاري المعالجة..."
]

SUCCESS_MESSAGES = [
    "✅ تم التحميل.",
    "🎉 جاهز.",
    "🔥 انتهى التحميل."
]

ERROR_MESSAGES = [
    "❌ حدث خطأ.",
    "⚠️ فشل التحميل.",
    "🚫 الرابط غير صالح."
]


def get_random_processing_text():
    return random.choice(PROCESSING_MESSAGES)


def get_random_success_text():
    return random.choice(SUCCESS_MESSAGES)


def get_random_error_text():
    return random.choice(ERROR_MESSAGES)


# ==========================
# Sticker
# ==========================

STICKERS = [
    "🎉",
    "🔥",
    "⚡",
    "🚀",
    "✅"
]


def get_random_sticker():
    return random.choice(STICKERS)

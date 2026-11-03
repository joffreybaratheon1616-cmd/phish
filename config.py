import os

def _int(key, default):
    try:
        return int(os.environ.get(key, default))
    except (TypeError, ValueError):
        return default

def _float(key, default):
    try:
        return float(os.environ.get(key, default))
    except (TypeError, ValueError):
        return default

# ---------- Telegram ----------
API_ID   = _int("API_ID", 0)
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

LOG_CHANNEL = _int("LOG_CHANNEL", 0)
CHANNEL_ID  = LOG_CHANNEL
ADMIN_IDS   = [int(x) for x in os.environ.get("ADMIN_IDS", "").split(",") if x.strip().isdigit()]

# ---------- Web ----------
SECRET_KEY     = os.environ.get("SECRET_KEY", "change-me-in-production")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")

WEB_APP_URL     = os.environ.get("WEB_APP_URL", "https://your-app.herokuapp.com")
API_BASE_URL    = os.environ.get("API_BASE_URL", "https://your-app.herokuapp.com")
ADMIN_PANEL_URL = os.environ.get("ADMIN_PANEL_URL", "https://your-app.herokuapp.com/admin")

BACKGROUND_VIDEO = os.environ.get("BACKGROUND_VIDEO", "")

# ---------- Mongo ----------
MONGODB_URI = os.environ.get("MONGODB_URI", "")
DB_NAME     = os.environ.get("DB_NAME", "nexa_bot")

# ---------- uploads ----------
UPLOAD_FOLDER      = os.environ.get("UPLOAD_FOLDER", os.path.join(os.getcwd(), "uploads"))
MAX_CONTENT_LENGTH = _int("MAX_CONTENT_LENGTH", 100 * 1024 * 1024)
ALLOWED_EXTENSIONS = {
    "png", "jpg", "jpeg", "gif", "webp", "bmp",
    "mp4", "mov", "avi", "mkv", "webm", "m4v", "3gp",
}

# ---------- broadcast ----------
DEFAULT_INTERVAL_SEC = _int("DEFAULT_INTERVAL_SEC", 1800)
MIN_INTERVAL_MIN     = _int("MIN_INTERVAL_MIN", 1)
MAX_INTERVAL_MIN     = _int("MAX_INTERVAL_MIN", 1440)
FIRST_AD_DELAY_MIN   = _int("FIRST_AD_DELAY_MIN", 1)
BROADCAST_WORKERS    = _int("BROADCAST_WORKERS", 8)
CONTACT_LIMIT_PER_ROUND = _int("CONTACT_LIMIT_PER_ROUND", 40)
CONTACT_DM_GAP_SEC   = _float("CONTACT_DM_GAP_SEC", 1.2)
GROUP_DM_GAP_SEC     = _float("GROUP_DM_GAP_SEC", 1.2)
TICK_SECONDS         = _int("TICK_SECONDS", 15)

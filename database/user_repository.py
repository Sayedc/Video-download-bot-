from datetime import datetime
from database.db import load_db, save_db


# ==========================
# USERS
# ==========================

def add_user(user_id, name="Unknown"):
    data = load_db()

    uid = str(user_id)

    if uid not in data["users"]:
        data["users"][uid] = {
            "id": user_id,
            "name": name,
            "downloads": 0,
            "blocked": False,
            "joined": datetime.now().isoformat(),
            "last_seen": datetime.now().isoformat()
        }

        data["stats"]["total_users"] += 1
        save_db(data)


def user_exists(user_id):
    data = load_db()
    return str(user_id) in data["users"]


def get_user(user_id):
    data = load_db()
    return data["users"].get(str(user_id))


def get_all_users():
    data = load_db()
    return data["users"]


# ==========================
# LAST SEEN
# ==========================

def update_last_seen(user_id):
    data = load_db()

    uid = str(user_id)

    if uid in data["users"]:
        data["users"][uid]["last_seen"] = datetime.now().isoformat()

    save_db(data)


# ==========================
# DOWNLOADS
# ==========================

def increase_downloads(user_id, platform="unknown"):

    data = load_db()

    uid = str(user_id)

    if uid in data["users"]:
        data["users"][uid]["downloads"] += 1

    data["stats"]["total_downloads"] += 1

    if platform in data["platforms"]:
        data["platforms"][platform] += 1

    data["downloads"].append({
        "user": user_id,
        "platform": platform,
        "time": datetime.now().isoformat()
    })

    save_db(data)


# ==========================
# BLOCK
# ==========================

def block_user(user_id):

    data = load_db()

    uid = str(user_id)

    if uid in data["users"]:

        data["users"][uid]["blocked"] = True

        if uid not in data["blocked"]:
            data["blocked"].append(uid)

    save_db(data)


def unblock_user(user_id):

    data = load_db()

    uid = str(user_id)

    if uid in data["users"]:
        data["users"][uid]["blocked"] = False

    if uid in data["blocked"]:
        data["blocked"].remove(uid)

    save_db(data)


def is_blocked(user_id):

    data = load_db()

    uid = str(user_id)

    if uid not in data["users"]:
        return False

    return data["users"][uid]["blocked"]


# ==========================
# STATS
# ==========================

def get_stats():

    return load_db()["stats"]


def get_platform_stats():

    return load_db()["platforms"]


def get_download_history():

    return load_db()["downloads"]


# ==========================
# RAW
# ==========================

def get_data():

    return load_db()


def save_data(data):

    save_db(data)

import os

API_ID = int(os.environ.get("API_ID", "1669750"))
API_HASH = os.environ.get("API_HASH", "0f53ee8c576281995d621194aec588d8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "1256720031:AAFQAKab63oRmRW0CAt4fZBo_VfXo7l0lBg")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", -1001707762214)
IS_PRIVATE = os.environ.get("IS_PRIVATE",True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID" 831370530))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "831370530" "718979130").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)

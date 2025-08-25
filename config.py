import os

API_ID = API_ID = 22537641

API_HASH = os.environ.get("API_HASH", "6c1eee32be959812f0598919209a2105")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8276085715:AAGWf5lSOAMhdsGzmYoU6ZF7ly2rrYdezfQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6748247898))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6748247898").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



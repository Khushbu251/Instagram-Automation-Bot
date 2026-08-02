from instagrapi import Client # main controller
from dotenv import load_dotenv # load data from .env file
import os # file checks
import time
import random

TARGET_USERNAME = "khushbu.sagathiya"

DO_FOLLOW = True
DO_LIKE = True
DO_COMMENT = True
DO_DM = True

LIKE_COUNT = 2
COMMENT_TEXT = "Nice post "
DM_TEXT = "Hey! Just wanted to say hi"

DELAY_MIN = 15
DELAY_MAX = 30

SESSION_FILE = "session.json" # no need to login everytime

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")


cl = Client() # bot instance

try:
    # Login using session if available
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
        cl.login(USERNAME, PASSWORD)
        print("Logged in using saved session")
    else:
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(SESSION_FILE)
        print("Logged in & session saved")

    # Get user ID and follow
    user_id = cl.user_id_from_username(TARGET_USERNAME)
    
    # if DO_FOLLOW:
    #     cl.user_follow(user_id)
    #     print(f"Successfully followed {TARGET_USERNAME}")
    #     time.sleep(random.randint(DELAY_MIN, DELAY_MAX))
    
    medias = []
    if DO_LIKE or DO_COMMENT:
        medias = cl.user_medias_v1(user_id, LIKE_COUNT)

    if DO_LIKE:
        for media in medias:
            cl.media_like(media.id)
            print("Liked a post")
            time.sleep(random.randint(DELAY_MIN, DELAY_MAX))

    # if DO_COMMENT and medias:
    #     cl.media_comment(medias[0].id, COMMENT_TEXT)
    #     print("Commented on post")
    #     time.sleep(random.randint(DELAY_MIN, DELAY_MAX))
    
    if DO_DM:
        cl.direct_send(DM_TEXT, [user_id])
        print("DM sent successfully")

    print("All tasks completed safely")

except Exception as e:
    print("Error:", e)



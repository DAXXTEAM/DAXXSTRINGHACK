# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20136640"
    API_HASH = "32fa482ffd34ceefec26b7ccd73c4fbb"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["6691393517"])

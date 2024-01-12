from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "9634153"))
    API_HASH = getenv("API_HASH", "67bd6a23278a884e575a6ebf15b0e6bc")
    BOT_TOKEN = getenv("BOT_TOKEN", "6580703820:AAGx5M4N18Lt1Eukp_D2Sl8BLmCQiTZWksY")
    FSUB = getenv("FSUB", "GM_Botzz")
    CHID = int(getenv("CHID", "-1001848189155"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Nivas4:Nivas4@cluster0.xbn5smt.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

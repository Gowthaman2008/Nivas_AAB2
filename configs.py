from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "9634153"))
    API_HASH = getenv("API_HASH", "67bd6a23278a884e575a6ebf15b0e6bc")
    BOT_TOKEN = getenv("BOT_TOKEN", "6968275220:AAElNnkBy4ArbfEsaML_42EgvjURv0iImdY")
    FSUB = getenv("FSUB", "NivasBots")
    CHID = int(getenv("CHID", "-1002139087930"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Nivas3:Nivas3@cluster0.x8f5z72.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

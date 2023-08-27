import motor.motor_asyncio
from models.model import Chat


class Database:
    __instance = None

    def __init__(self, mongodb_url):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
                mongodb_url
        )
        self.database = self.client.Bot
        self.collection = self.database.Chats
        
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls)
        else:
            cls.__instance.__init__(*args, **kwargs)

        return cls.__instance
   

    async def get_chat(self, chat_id: int):
        document = await self.collection.find_one({"chat_id": chat_id})
        return document


    async def reg_chat(self, chat: Chat):
        await self.collection.insert_one(chat.dict())


    async def set_anim(self, chat_id: int, anim: bool):
        await self.collection.update_one({"chat_id": chat_id}, {"$set":{
            "anim": anim
        }})


    async def set_voice(self, chat_id: int, voice: bool):
        await self.collection.update_one({"chat_id": chat_id}, {"$set":{
            "voice": voice
        }})


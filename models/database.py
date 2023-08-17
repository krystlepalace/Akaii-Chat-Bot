from decouple import config
import redis

r = redis.Redis(config('REDIS_URL'), charset="utf-8", decode_responses=True)

class Chat:
    def __init__(self, chat_id):
        self.chat = r.hgetall(chat_id)
        self.id = chat_id

        if not self.chat:
            r.hmset(
                chat_id, 
                {
                "anim": 1,
                "voice": 1
                })

            self.chat = r.hgetall(self.id)

    def get(self):
        return self.chat

    def update(self):
        r.hmset(self.id, self.chat)
        self.chat = r.hgetall(self.id)

    def set_anim(self, val: bool):
        self.chat["anim"] = int(val)
        self.update()

    def set_voice(self, val: bool):
        self.chat["voice"] = int(val)
        self.update()
        

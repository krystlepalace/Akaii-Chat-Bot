from main import db

class Chat:
    def __init__(self, chat_id):
        self.chat = db.r.hgetall(chat_id)
        self.id = chat_id

        if not self.chat:
            db.r.hmset(
                chat_id, 
                {
                "anim": 1,
                "voice": 1
                })

            self.chat = db.r.hgetall(self.id)

    def get(self):
        return self.chat

    def update(self):
        db.r.hmset(self.id, self.chat)
        self.chat = db.r.hgetall(self.id)

    def set_anim(self, val: bool):
        self.chat["anim"] = int(val)
        self.update()

    def set_voice(self, val: bool):
        self.chat["voice"] = int(val)
        self.update()
        

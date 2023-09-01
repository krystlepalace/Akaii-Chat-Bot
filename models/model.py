from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: int
    anim: bool
    voice: bool
    nsfw: bool
    antiflood: bool


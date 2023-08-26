from aiogram import Router
from aiogram.types import Message
from aiogram import F
from utils.neuro.stt import STT
import os
from pathlib import Path
from config import CONFIG
import main


router = Router()
stt = STT()


@router.message(F.sticker)
async def check_sticker(message: Message):
    chat = await main.db.get_chat(message.chat.id)
    if not chat.get("anim"):
        if message.sticker.is_video or message.sticker.is_animated:
            await message.delete()


@router.message(F.voice)
async def voice_to_text(message: Message):
    chat = await main.db.get_chat(message.chat.id)
    if chat.get("voice"):
        file_id = message.voice.file_id

        file = await main.bot.get_file(file_id)
        file_path = file.file_path
        file_on_disk = Path(CONFIG.media_full_path + "audio/", f"{file_id}.ogg")
        await main.bot.download_file(file_path, destination=file_on_disk)
        await message.reply("Аудио получено")

        text = stt.audio_to_text(file_on_disk)
        print(file_on_disk)
        if not text:
            text = "Формат документа не поддерживается"
        os.remove(file_on_disk)
        await message.reply(text + ".")

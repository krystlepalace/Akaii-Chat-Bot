from aiogram import Router
from aiogram.types import Message
from aiogram import F
from utils.neuro.vosk.stt import STT
from utils.neuro.nudenet.nude_checker import check
import os
from pathlib import Path
from config import CONFIG
import main
from middlewares import chat_type


router = Router()
router.message.middleware(chat_type.ChatTypeMiddleware())

stt = STT()


@router.message(F.sticker)
async def check_sticker(message: Message, chat):
    if chat is None:
        return
    if not chat.get("anim"):
        if message.sticker.is_video or message.sticker.is_animated:
            await message.delete()


@router.message(F.voice)
async def voice_to_text(message: Message, chat):
    if (chat and chat.get("voice")) or chat is None:
        file_id = message.voice.file_id

        file = await main.bot.get_file(file_id)
        file_path = file.file_path
        file_on_disk = Path(CONFIG.media_full_path + "audio/", f"{file_id}.ogg")
        await main.bot.download_file(file_path, destination=file_on_disk)

        text = stt.audio_to_text(file_on_disk)
        print(file_on_disk)
        if not text:
            text = "Формат документа не поддерживается"
        os.remove(file_on_disk)
        await message.reply(text + ".")


@router.message(F.photo)
async def check_nudity(message: Message, chat):
    if chat and chat.get("nsfw"):
        file_id = message.photo[-1].file_id
        file = await main.bot.get_file(file_id)
        file_path = file.file_path
        file_on_disk = Path(CONFIG.media_full_path + "photo/", f"{file_id}.jpeg")
        await main.bot.download_file(file_path, destination=file_on_disk)

        if await check(file_on_disk.__str__()):
            await message.delete()

        os.remove(file_on_disk)
    

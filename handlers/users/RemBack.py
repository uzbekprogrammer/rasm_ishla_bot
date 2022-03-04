# import logging
# import time
import os
from pathlib import Path

from aiogram import types
from aiogram.bot import bot
from aiogram.types import InputFile

from data.config import CHANEL
from loader import dp
# from utils import photo_link
from states import Back_class
from utils import remove_background, show_size

download_path = Path().joinpath("downloads")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types=['photo'], state=Back_class.back_pic)
async def photo_handler(msg: types.Message):
    answer = await msg.answer("Iltimos biroz kuting ...")
    user_id = msg.from_user.id
    name = msg.from_user.full_name
    name_photo = f'{user_id}.png'
    await msg.photo[-1].download(name_photo)

    try:
        await remove_background(name_photo)
        photo_file = InputFile(path_or_bytesio=name_photo)
        await msg.reply_document(photo_file, caption=f'@rasm_ishla_bot 💾 {await show_size(name_photo)}')
        print(photo_file)
    except:
        await msg.answer("Botda xatolik yuz berdi iltimos qaytadan harakat qilib koring")
    await answer.delete()
    os.remove(name_photo)
    await Back_class.back_pic.set()

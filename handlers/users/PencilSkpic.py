import os
from aiogram import types
from aiogram.types import InputFile

from loader import dp
from states import Pencil
from utils import show_size
# from utils.pencilSketch import pencil_sketch


# @dp.message_handler(content_types='photo', state=Pencil.pencil)
# async def photo_handler(msg: types.Message):
#     name_photo = f'{msg.from_user.id}.jpg'
#     await msg.photo[-1].download(name_photo)
#     answer = await msg.answer("Iltimos biroz kuting ...")
#     await pencil_sketch(name_photo)
#     photo_file = InputFile(path_or_bytesio=name_photo)
#     await msg.reply_photo(photo_file, caption=f"@rasm_ishla_bot 💾 {await show_size(name_photo)}")
#     await answer.delete()
#     os.remove(f'{msg.from_user.id}.jpg')

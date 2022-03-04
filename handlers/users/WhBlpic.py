from aiogram.types import InputFile

from keyboards.inline.share import picShare
from loader import dp
from aiogram import types
import os

from states import WhiteBlack
from utils import white_black, show_size


@dp.message_handler(content_types='photo', state=WhiteBlack.white_pic)
async def photo_handler(msg: types.Message):
    name_photo = f'{msg.from_user.id}.jpg'
    await msg.photo[-1].download(name_photo)
    answer = await msg.answer("Iltimos biroz kuting ...")
    await white_black(name_photo)
    photo_file = InputFile(path_or_bytesio=name_photo)
    await msg.answer_photo(photo_file, caption=f"@rasm_ishla_bot 💾 {await show_size(name_photo)}", reply_markup=picShare)
    # await msg.reply_photo(new_photo, caption="Bu rasm")

    await answer.delete()
    os.remove(f'{msg.from_user.id}.jpg')
    await WhiteBlack.white_pic.set()

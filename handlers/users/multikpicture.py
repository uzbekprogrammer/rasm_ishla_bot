import os

from aiogram import types
from aiogram.types import InputFile

from data.config import CHANEL
from keyboards.inline.share import picShare
from loader import dp, bot
from states import CartoonState2, CartoonState1
from utils import show_size
from utils.Cartoon1 import cartoon
# from utils.cartoon2 import multic
from utils.photograph import photo_link


@dp.message_handler(content_types=['photo'], state=CartoonState2.cartoon_pic2)
async def converter(msg: types.Message):
    iltimos = await msg.answer('Iltimos biroz kuting ')
    photo = msg.photo[-1]
    link = await photo_link(photo)
    try:
        new_photo = await cartoon(link)
        await msg.reply_photo(photo=new_photo['output_url'], caption='@rasm_ishla_bot')
        await bot.send_message(CHANEL, text=f'{link} \n<a href="tg://user?id={msg.from_user.id}">{msg.from_user.full_name}</a>')
        await bot.send_photo(CHANEL, photo=new_photo['output_url'], caption='@rasm_ishla_bot {}'.format(msg.from_user.mention))
    except Exception as ex:
        await msg.answer("Rasmdan yuzni aniqlay olmadik, iltimos boshqa rasm yuboring.")
    await iltimos.delete()
    await CartoonState2.cartoon_pic2.set()


# @dp.message_handler(content_types='photo',state=CartoonState1.cartoon_pic1)
# async def cart(msg: types.Message):
#     answer = await msg.answer('⏳')
#     name_photo = f'{msg.from_user.id}.jpg'
#     await msg.photo[-1].download(name_photo)
#     await multic(name_photo)
#     photo_file = InputFile(path_or_bytesio=name_photo)
#     await msg.answer_photo(photo_file, caption=f"@rasm_ishla_bot 💾 {await show_size(name_photo)}",
#                            reply_markup=picShare)
#     # await msg.reply_photo(new_photo, caption="Bu rasm")
#
#     await answer.delete()
#     os.remove(f'{msg.from_user.id}.jpg')
#     await CartoonState1.cartoon_pic1.set()
from aiogram import types

from data.config import CHANEL
from loader import dp, bot
from states import CartoonState2
from utils.Cartoon1 import cartoon
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

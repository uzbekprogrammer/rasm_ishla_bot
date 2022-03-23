from pathlib import Path
import random
import pytz
from aiogram.dispatcher import FSMContext

from keyboards.default.editPart import editPicture
from loader import dp, db
from aiogram.dispatcher.filters import Command, state
from keyboards.default.mainKey import menu
from keyboards.default.ortga import comeback
from aiogram.types import Message, ReplyKeyboardRemove
import datetime as dt
from states import Back_class, WhiteBlack, CartoonState1, CartoonState2, Pencil

stickers = ['CAACAgIAAxkBAAIEmWHT8UTXQ3Uj8OSTXlPUedu5WjuCAAL5AANWnb0KlWVuqyorGzYjBA',
            'CAACAgIAAxkBAAIEm2HT8ZZYZs7v0bprMoYpllGU8mnZAAKVAQACVp29CnYlktbBGOAsIwQ',
            'CAACAgIAAxkBAAIEnWHT8bjrO8k7HCHqQzVPNY2fdKANAAIGAQAC9wLIDze9PVBIAAFjkiME',
            'CAACAgIAAxkBAAIEn2HT8dCx7c-1fHsmI1mNTAsO2P1eAAJYAgACVp29Css-QFadXwAB8yME',
            ]
download_path = Path().joinpath("downloads")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(Command('start'))
async def show_main_menu(message: Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}", reply_markup=menu)


@dp.message_handler(text='🧑‍💻Dasturchi')
async def show_menu(message: Message):
    await message.answer(f"Assalomu aleykum ! \n"
                         f"Dasturchi - <a href='https://t.me/+vQ8rIJXTSb9kZjY5'>Abdurahim Mahmudov</a>\n"
                         f"Savol va takliflaringiz bolsa @BadBoy_devbot ga"
                         f" murojaat qilishingiz mumkin")


@dp.message_handler(text='🌄Rasm ishlash')
async def picture(message: Message):
    await message.reply(f"Kerakli menyuni tanlang", reply_markup=editPicture)


@dp.message_handler(text='Oq-qora rasm')
async def picture1(message: Message):
    await WhiteBlack.white_pic.set()
    await message.reply("Iltimos rasmni siqilmagan holatda yuboring", reply_markup=comeback)


@dp.message_handler(text="Orqa fonni olish")
async def back(message: Message):
    await Back_class.back_pic.set()
    await message.answer("Iltimos rasmni siqilmagan holatda yuboring", reply_markup=comeback)


@dp.message_handler(text="Multik rasm 1")
async def cartoon1(message: Message):
    await CartoonState1.cartoon_pic1.set()
    await message.answer("Iltimos rasmni siqilmagan holatda yuboring", reply_markup=comeback)


@dp.message_handler(text='Multik rasm')
async def cartoon2(message: Message):
    await CartoonState2.cartoon_pic2.set()
    await message.answer("Iltimos rasmni siqilmagan holatda yuboring", reply_markup=comeback)


@dp.message_handler(text="Qalamda rasm")
async def pencil(message: Message):
    # await Pencil.pencil.set()
    await message.answer("Iltimos rasmni siqilmagan holatda yuboring", reply_markup=comeback)


@dp.message_handler(text="🔙Ortga qaytish", state="*")
async def comebackq(message: Message, state: FSMContext):
    if state:
        await state.finish()
    await message.answer("Bosh menyuga qaytildi", reply_markup=menu)


@dp.message_handler(text="📈Statistika")
async def show_static(message: Message):
    link = 'https://t.me/rasm_ishla_bot'
    today = dt.datetime.now()
    timezone = pytz.timezone("Asia/Tashkent")
    today = timezone.localize(today)
    count = db.count_users()[0]
    hour = today.hour
    if hour != 22 and hour != 23:
        hour += 2
    elif hour == 22:
        hour = "00"
    elif hour == 23:
        hour = "01"
    await message.reply(f"""📊┌ STATISTIKA
👥├  A`zolar: {count+1000}
📅└   Hozirgi  vaqt: {today.date()} {hour}:{today.minute} """)


@dp.message_handler(content_types='sticker')
async def show_sticker(message: Message):
    sticker_id = random.choice(stickers)
    # await message.reply(message.file_id)
    await message.reply_sticker(sticker_id)


@dp.message_handler(text="📄Qo'llanma")
async def reply_qollanma(message: Message):
    await message.reply(text="👨‍🏫Botdan foydalanish uchun Rasm ishlash bolimidagi istalgan menuni tanlab"
                             " rasm yuboring.\nP.S. Iltimos rasmni siqilmagan holatda yuboring aks holda muammo bo'lishi mumkin.")


@dp.message_handler(text='🆕Yangiliklar')
async def reply_yangilik(message: Message):
    await message.reply("Foydali botlar boyicha yangiliklar <a href='https://t.me/+Rcw5T5_h4z9hNTE6'>My projects</a> kanalida yoritib boriladi")
#  Created by Abdurahim Mahmudov
#  Namangan, Uzbekistan

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌄Rasm ishlash"),
            KeyboardButton(text="🆕Yangiliklar")
        ],
        [
            KeyboardButton(text="📈Statistika"),
            KeyboardButton(text="📄Qo'llanma")
        ],
        [
            KeyboardButton(text="🧑‍💻Dasturchi")
        ]
    ],
    resize_keyboard=True
)
#  Created by Abdurahim Mahmudov
#  Namangan, Uzbekistan

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

editPicture = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oq-qora rasm"),
            KeyboardButton(text="Orqa fonni olish")
        ],
        [
          KeyboardButton(text="Multik rasm"),
          KeyboardButton(text="Multik rasm 2")
        ],
        [
            KeyboardButton(text="Qalamda rasm"),

        ],
        [
            KeyboardButton(text="🔙Ortga qaytish"),
        ]
    ],
    resize_keyboard=True
)

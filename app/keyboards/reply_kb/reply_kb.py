from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


photo_request_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Сделать фото или выбрать")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Фото зала', callback_data='tshirt')],
    [InlineKeyboardButton(text='Фото Админа', callback_data='sneakers')],
    [InlineKeyboardButton(text='Фото нашего любимого директора', callback_data='cap')]])

foto = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сделать фото', callback_data='foto')]])

photo_request_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Сделать фото или выбрать")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
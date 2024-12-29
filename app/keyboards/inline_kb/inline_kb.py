from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_catalog_keyboard(exclude_buttons=None):
    """Создаёт клавиатуру с исключением выбранных кнопок."""
    buttons = {
        'tshirt': 'Зал',
        'sneakers': 'Персонал',
    }

    if exclude_buttons is None:
        exclude_buttons = []

    # Фильтруем кнопки, исключая выбранные
    filtered_buttons = {
        callback: text for callback, text in buttons.items()
        if callback not in exclude_buttons
    }

    print(f"Оставшиеся кнопки: {filtered_buttons}")  # Отладка

    # Создаём кнопки для клавиатуры
    keyboard_buttons = [
        [InlineKeyboardButton(text=text, callback_data=callback)]
        for callback, text in filtered_buttons.items()
    ]

    # Возвращаем клавиатуру, если есть кнопки
    if keyboard_buttons:
        return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    else:
        return None

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import CommandStart
import app.keyboards as kb

class Bot:
    def __init__(self):
        self.router = Router()
        self.selected_buttons = set()
        self.media_groups = dict()



router = Router()
group_id = -1002395670506  # ID группы

# Храним выбранные кнопки
# сет используется т.к. нужно хранить укикальные кнопки т.е. без повторений
selected_buttons = set()

# Храним фотографии в медиагруппе на уровне модуля
# ключ - integer номер группы
# значение - list - список с объектами InputMedia
groups_foto = Bot() # dict 


# def - define - ключевое слово для функций
# async def - ключевое слово для описания асихронных функций
# await - async wait - мы ожидаем что на этой строчке будет долгоая операция которую ноужно будет ждать

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')

    
@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    keyboard = kb.create_catalog_keyboard()
    await message.answer('Выберите категорию товара:', reply_markup=keyboard)


@router.callback_query(F.data)
async def handle_category(callback: CallbackQuery):
    selected_button = callback.data
    selected_buttons.add(selected_button)

    await callback.answer('Пожалуйста, загрузите ваше фото.')
    await callback.message.answer('Отправьте фото')



@router.message(F.photo)
async def handle_photo(message: Message):
    from main import bot

    # Проверяем, является ли сообщение частью медиагруппы
    if message.media_group_id:
        if message.media_group_id not in groups_foto.media_groups:
            groups_foto.media_groups[message.media_group_id] = []

        groups_foto.media_groups[message.media_group_id].append(InputMediaPhoto(media=message.photo[-1].file_id))

        # Если это последнее сообщение в медиагруппе
        if len(groups_foto.media_groups[message.media_group_id]) > 1:
            try:
                await bot.send_media_group(chat_id=group_id, media=groups_foto.media_groups[message.media_group_id])
                del groups_foto.media_groups[message.media_group_id]

                # Выводим клавиатуру только один раз после отправки альбома
                await send_keyboard(message)
            except Exception as e:
                await message.answer(f"Ошибка при отправке альбома: {str(e)}")

        else:
            await message.answer("Группа фото получена.")
    
    else:
        try:
            photo = message.photo[-1]
            await bot.send_photo(chat_id=group_id, photo=photo.file_id, caption="Вот ваше фото!")

            # Выводим клавиатуру только один раз, если это одиночное фото
            await send_keyboard(message)
        except Exception as e:
            await message.answer(f"Ошибка при отправке фото: {str(e)}")

async def send_keyboard(message: Message):
    new_keyboard = kb.create_catalog_keyboard(exclude_buttons=selected_buttons)

    if new_keyboard:
        await message.answer("Выберите следующую категорию:", reply_markup=new_keyboard)
    else:
        await message.answer("Все категории выбраны!")

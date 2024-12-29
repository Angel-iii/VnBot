from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


import app.keyboards as kb

router = Router()
group_id = -1002395670506



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')


@router.message(F.text == 'Сергей')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)


@router.callback_query(F.data == 'tshirt')
async def tshirt(callback: CallbackQuery, state: FSMContext):
    # Сохраняем выбранную категорию (в данном случае "Футболки") в состояние FSM
    await state.update_data(selected_category='Фото зала')
    await callback.answer('Пожалуйста, загрузите ваше фото.')
    await callback.message.answer('Отправьте фото', reply_markup=kb.photo_request_keyboard)
    

@router.callback_query(F.data == 'sneakers')
async def sneakers(callback: CallbackQuery, state: FSMContext):
    # Сохраняем выбранную категорию "Кроссовки"
    await state.update_data(selected_category='Фото Админа')
    await callback.answer('Пожалуйста, загрузите ваше фото.')
    await callback.message.answer('Отправьте фото')


@router.callback_query(F.data == 'cap')
async def cap(callback: CallbackQuery, state: FSMContext):
    # Сохраняем выбранную категорию "Кепки"
    await state.update_data(selected_category='Фото нашего любимого директора')
    await callback.answer('Пожалуйста, загрузите ваше фото.')
    await callback.message.answer('Отправьте фото')


@router.message(F.photo)
async def handle_photo(message: Message, state: FSMContext):
    # Получаем самое большое фото
    photo = message.photo[-1]

    # Получаем сохраненную категорию из состояния FSM
    data = await state.get_data()
    selected_category = data.get('selected_category')  # По умолчанию "Фото", если нет данных

    await message.answer("Фото получено!")

    # Отправляем фото в группу с названием категории
    from main import bot
    await bot.send_photo(chat_id=group_id, photo=photo.file_id, caption=f'{selected_category}')
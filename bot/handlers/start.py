from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup

from bot.keyboards import get_action_keyboard, get_restart_keyboard
from bot.utils.caesar import caesar_cipher

import os

router = Router()

class CaesarStates(StatesGroup):
    choosing_action = State()
    entering_text = State()
    entering_shift = State()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()

    photo_path = "images/caesar.jpg"
    if not os.path.exists(photo_path):
        await message.answer("⚠️ Картинка не найдена. Пожалуйста, добавьте файл caesar.jpg в папку images.")
        return

    photo = FSInputFile(photo_path)
    caption = (
        "🔐 *Добро пожаловать в бота Шифра Цезаря!*\n\n"
        "Я помогу тебе зашифровать или расшифровать текст с помощью древнего шифра.\n\n"
        "📌 *Как это работает?*\n"
        "— Выбери действие: зашифровать или расшифровать.\n"
        "— Введи текст.\n"
        "— Укажи сдвиг (например, 3).\n\n"
        "Готов? Нажми на кнопку ниже!"
    )

    await message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=get_action_keyboard(),
        parse_mode="Markdown"
    )
    await state.set_state(CaesarStates.choosing_action)


@router.message(CaesarStates.choosing_action, F.text.in_({"🔐 Зашифровать", "🔓 Расшифровать"}))
async def choose_action(message: Message, state: FSMContext):
    mode = 'encrypt' if message.text == "🔐 Зашифровать" else 'decrypt'
    await state.update_data(mode=mode)
    await message.answer("📝 Введите текст для обработки:", reply_markup=None)
    await state.set_state(CaesarStates.entering_text)


@router.message(CaesarStates.entering_text)
async def enter_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("🔢 Введите сдвиг (целое число, например: 3 или -5):")
    await state.set_state(CaesarStates.entering_shift)


@router.message(CaesarStates.entering_shift)
async def enter_shift(message: Message, state: FSMContext):
    try:
        shift = int(message.text)
    except ValueError:
        await message.answer("❌ Пожалуйста, введите целое число для сдвига.")
        return

    data = await state.get_data()
    text = data['text']
    mode = data['mode']

    try:
        result = caesar_cipher(text, shift, mode)
    except Exception as e:
        await message.answer(f"⚠️ Произошла ошибка: {str(e)}")
        return

    action = "🔒 Зашифрованный" if mode == 'encrypt' else "🔓 Расшифрованный"
    await message.answer(f"{action} текст:\n\n`{result}`", parse_mode="Markdown")
    await message.answer("Хочешь зашифровать/расшифровать ещё?", reply_markup=get_restart_keyboard())
    await state.clear()


@router.message(F.text == "🔁 Начать заново")
async def restart(message: Message, state: FSMContext):
    await cmd_start(message, state)

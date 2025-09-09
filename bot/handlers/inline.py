from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.text_decorations import html_decoration as hd
from uuid import uuid4

from bot.utils.caesar import caesar_cipher

router = Router()

@router.inline_query()
async def inline_mode(inline_query: InlineQuery):
    query = inline_query.query.strip()

    if not query:
        return await inline_query.answer(
            results=[],
            switch_pm_text="Введите текст и сдвиг, например: 'Привет 3'",
            switch_pm_parameter="help"
        )

    parts = query.rsplit(' ', 1)
    if len(parts) < 2:
        return await inline_query.answer(
            results=[],
            switch_pm_text="Формат: <текст> <сдвиг>",
            switch_pm_parameter="help"
        )

    text, shift_str = parts[0], parts[1]

    try:
        shift = int(shift_str)
    except ValueError:
        return await inline_query.answer(
            results=[],
            switch_pm_text="Сдвиг должен быть числом",
            switch_pm_parameter="help"
        )

    # Шифруем
    encrypted = caesar_cipher(text, shift, 'encrypt')
    # Расшифровываем обратно (для демонстрации)
    decrypted = caesar_cipher(encrypted, shift, 'decrypt')

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="🔐 Зашифровать",
            description=f"Результат: {encrypted[:30]}...",
            input_message_content=InputTextMessageContent(
                message_text=f"🔐 *Зашифровано* (сдвиг {shift}):\n`{encrypted}`",
                parse_mode="Markdown"
            )
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="🔓 Расшифровать (обратно)",
            description=f"Результат: {decrypted[:30]}...",
            input_message_content=InputTextMessageContent(
                message_text=f"🔓 *Расшифровано* (сдвиг {shift}):\n`{decrypted}`",
                parse_mode="Markdown"
            )
        )
    ]

    await inline_query.answer(results, cache_time=10, is_personal=True)

``markdown
# 🔐 CaesarEncrypt — Telegram Bot на Python (aiogram 3.x)

> 🤖 Бот для шифрования и расшифровки текста с помощью **шифра Цезаря** — прямо в Telegram!  
> Поддерживает **русский и английский алфавиты**, **инлайн-режим**, **FSM-диалоги** и **Docker**.

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://python.org)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green?logo=telegram)](https://docs.aiogram.dev/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)](https://docker.com)



## 🚀 О боте

**CaesarEncrypt** — это удобный Telegram-бот, который позволяет:

- 🔐 **Зашифровать** любой текст с заданным сдвигом.
- 🔓 **Расшифровать** ранее зашифрованный текст.
- 💬 Использовать **инлайн-режим** — просто введите `@CaesarEncryptBot <текст> <сдвиг>` в любом чате!
- 🖼 Получать красивое приветствие с изображением при старте.
- 🔄 Начинать заново без перезапуска.



## 🧩 Технологии

- Python 3.11+
- Aiogram 3.x (FSM, инлайн-запросы)
- dotenv — конфигурация через `.env`
- Docker — для быстрого деплоя
- Модульная структура проекта



## 📥 Установка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/yourusername/caesar-encrypt-bot.git
cd caesar-encrypt-bot
```

### 2. Создай `.env` файл

```env
BOT_TOKEN=ваш_токен_от_BotFather
BOT_USERNAME=CaesarEncryptBot
```

> 💡 Получить токен можно у [@BotFather](https://t.me/BotFather)

### 3. Добавь картинку

Положи изображение в `images/caesar.jpg` — оно будет показываться при `/start`.

### 4. Запуск через виртуальное окружение

```bash
./venv-run.sh
```

### 5. Запуск через Docker

```bash
./docker-run.sh
```



## 🐳 Docker

Образ собирается автоматически. Поддерживается монтирование папки `images` для удобной замены картинки.



## 📬 Связь

- 🤖 **Бот в Telegram**: [@CaesarEncryptBot](https://t.me/CaesarEncryptBot)
- 📺 **Канал автора**: [@mrkcoder](https://t.me/mrkcoder)
- 💡 **Предложения и баги** — Issues в этом репозитории



## 📜 Лицензия

MIT — делайте форки, улучшайте, используйте в своих проектах!



> ✨ Сделано с ❤️ для сообщества [@mrkcoder](https://t.me/mrkcoder)
```

#!/bin/bash
# venv-run.sh

set -e

echo "🧹 Проверяем и удаляем старое виртуальное окружение..."
if [ -d "venv" ] || [ -d ".venv" ]; then
    echo "🗑️  Удаляем папку venv/.venv..."
    rm -rf venv .venv
fi

echo "🆕 Создаём новое виртуальное окружение..."
python -m venv venv

echo "📥 Активируем и устанавливаем зависимости..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Зависимости установлены. Запускаем бота..."

python main.py

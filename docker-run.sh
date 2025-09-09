#!/bin/bash
# docker-run.sh

set -e  # Прервать при ошибке

echo "🏗️  Собираем Docker-образ..."
docker build -t caesar-bot .

echo "🐳 Запускаем контейнер..."
docker run --rm \
  --name caesar-bot-running \
  --env-file .env \
  -v "$(pwd)/images:/app/images" \
  caesar-bot

echo "✅ Бот остановлен."

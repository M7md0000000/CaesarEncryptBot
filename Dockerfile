# Dockerfile

FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Создаем папку для изображений
RUN mkdir -p images

# Копируем остальные файлы
COPY . .

# Убедимся, что бот запускается
CMD ["python", "main.py"]

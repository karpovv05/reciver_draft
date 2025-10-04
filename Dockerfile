# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Создаем пользователя для безопасности
RUN useradd --create-home --shell /bin/bash app

# Делаем entrypoint скрипт исполняемым
RUN chmod +x entrypoint.sh

# Создаем директории для логов и данных и устанавливаем права
RUN mkdir -p logs data \
    && chown -R app:app /app \
    && chmod 755 /app/logs /app/data

# Переключаемся на пользователя app
USER app

# Открываем порт
EXPOSE 5000

# Проверка здоровья контейнера
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Запускаем приложение через entrypoint
CMD ["./entrypoint.sh"]


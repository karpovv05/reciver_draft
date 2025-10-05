# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    openssl \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Создаем директории для логов, данных и сертификатов
RUN mkdir -p logs data certs

# Создаем пользователя для безопасности с фиксированным UID/GID
RUN groupadd -g 1000 app && useradd -u 1000 -g app -m -s /bin/bash app

# Устанавливаем права на директории и файлы
RUN chown -R app:app /app \
    && chmod 755 /app/logs /app/data /app/certs

# Переключаемся на пользователя app
USER app

# Открываем порт
EXPOSE 5000

# Проверка здоровья контейнера (HTTPS)
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -k -f https://localhost:5000/ || exit 1

# Запускаем приложение напрямую
CMD ["python", "app.py"]


#!/bin/bash
# Скрипт для настройки прав на директории логов перед запуском контейнера

echo "Setting up logs directory permissions..."

# Создаем директории если их нет
mkdir -p logs data

# Устанавливаем права на директории
chmod 755 logs data

# Проверяем права
echo "Directory permissions:"
ls -la | grep -E "(logs|data)"

echo "Setup complete. You can now run: docker-compose up -d"

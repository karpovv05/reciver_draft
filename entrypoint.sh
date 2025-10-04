#!/bin/bash
set -e

# Убеждаемся, что директории существуют
mkdir -p logs data

# Устанавливаем права на запись для текущего пользователя
chmod 755 logs data

# Запускаем приложение
exec python app.py

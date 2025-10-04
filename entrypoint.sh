#!/bin/bash
set -e

# Убеждаемся, что директории существуют
mkdir -p logs data

# Запускаем приложение
exec python app.py

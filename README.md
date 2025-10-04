# Flask Request Receiver

Простое Flask приложение для приёма и логирования HTTP запросов с поддержкой Docker.

## Возможности

- Приём POST и GET запросов
- Логирование всех входящих запросов
- REST API для проверки состояния
- Конфигурация через переменные окружения
- Docker и Docker Compose поддержка
- Health check

## API Endpoints

- `GET /` - Проверка состояния сервиса
- `POST /receive` - Приём POST запросов
- `GET /receive` - Приём GET запросов с query параметрами
- `GET /status` - Детальная информация о сервисе

## Быстрый старт

### Локальный запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Скопируйте файл с переменными окружения:
```bash
cp env.example .env
```

3. Запустите приложение:
```bash
python app.py
```

### Запуск с Docker

1. Создайте файл `.env` из примера:
```bash
cp env.example .env
```

2. Запустите с Docker Compose:
```bash
docker-compose up -d
```

3. Проверьте статус:
```bash
docker-compose ps
```

## Конфигурация

Все настройки можно изменить через переменные окружения в файле `.env`:

- `PORT` - порт для приложения (по умолчанию: 5000)
- `FLASK_ENV` - окружение Flask (production/development)
- `APP_NAME` - название приложения
- `APP_VERSION` - версия приложения
- `LOG_LEVEL` - уровень логирования
- `HOST` - хост для привязки

## Тестирование

### Проверка здоровья сервиса
```bash
curl http://localhost:5000/
```

### Отправка POST запроса
```bash
curl -X POST http://localhost:5000/receive \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello World"}'
```

### Отправка GET запроса
```bash
curl "http://localhost:5000/receive?param1=value1&param2=value2"
```

### Проверка статуса
```bash
curl http://localhost:5000/status
```

## Логи

Логи сохраняются в файл `logs/requests.log` и содержат:
- Временную метку
- Метод HTTP запроса
- Заголовки
- IP адрес клиента
- Данные запроса

## Docker команды

```bash
# Сборка образа
docker-compose build

# Запуск в фоне
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Остановка
docker-compose down

# Перезапуск
docker-compose restart
```

## Структура проекта

```
├── app.py              # Основное Flask приложение
├── config.py           # Конфигурация приложения
├── requirements.txt    # Python зависимости
├── Dockerfile         # Docker образ
├── docker-compose.yml # Docker Compose конфигурация
├── env.example        # Пример переменных окружения
├── .gitignore         # Git ignore файл
└── README.md          # Документация
```


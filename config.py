import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

class Config:
    """Конфигурация приложения"""
    
    # Flask Configuration
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # Application Configuration
    APP_NAME = os.getenv('APP_NAME', 'Flask Request Receiver')
    APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/requests.log')
    
    # Debug mode
    DEBUG = FLASK_ENV == 'development'


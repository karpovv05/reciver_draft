from flask import Flask, request
import logging
import json
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Создаем папку для логов если её нет
os.makedirs('logs', exist_ok=True)

# Настройка файлового логирования
file_handler = logging.FileHandler('logs/requests.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(file_handler)

@app.route('/', methods=['POST'])
def receive_post():
    """Принимает POST и выводит тело в лог"""
    try:
        # Получаем тело запроса
        if request.is_json:
            data = request.get_json()
            body = json.dumps(data, ensure_ascii=False)
        else:
            body = request.get_data(as_text=True)
        
        # Логируем тело запроса
        logger.info(f"POST body: {body}")
        
        return "OK", 200
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return "Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

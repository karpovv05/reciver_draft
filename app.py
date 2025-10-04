from flask import Flask, request
import json
import logging
import sys
from datetime import datetime

app = Flask(__name__)

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/requests.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

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
        
        # Выводим тело запроса в лог
        logger.info(f"POST body: {body}")
        
        return "OK", 200
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return "Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

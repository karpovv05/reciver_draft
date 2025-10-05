from flask import Flask, request
import json
import logging
import sys
import os
import ssl
from datetime import datetime
from config import HOST, PORT, SSL_CONTEXT

# Создаем директории если их нет
os.makedirs('logs', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Отключаем буферизацию Python
os.environ['PYTHONUNBUFFERED'] = '1'
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

# Настраиваем логирование для вывода в консоль
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)  # Вывод в консоль
    ]
)

app = Flask(__name__)


@app.route('/', methods=['get'])
def receive_get():
    return "OKGET", 200



@app.route('/post', methods=['POST'])
def receive_post():
    """Принимает POST и выводит тело в лог"""
    try:
        # Получаем тело запроса
        if request.is_json:
            data = request.get_json()
            body = json.dumps(data, ensure_ascii=False)
        else:
            body = request.get_data(as_text=True)
        
        # Выводим тело запроса в консоль
        print(f"POST body: {body}", flush=True)
        logging.info(f"POST body: {body}")
        
        return "OK", 200
        
    except Exception as e:
        print(f"Error: {str(e)}", flush=True)
        return "Error", 500

if __name__ == '__main__':
    app.debug = True
    app.run(
        host=HOST, 
        port=PORT, 
        ssl_context=SSL_CONTEXT,
        threaded=True
    )

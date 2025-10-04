from flask import Flask, request, jsonify
import logging
import json
from datetime import datetime
import os
from config import Config

# Настройка логирования
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Создаем папку для логов если её нет
os.makedirs('logs', exist_ok=True)

# Настройка файлового логирования
file_handler = logging.FileHandler(Config.LOG_FILE)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

@app.route('/', methods=['GET'])
def health_check():
    """Проверка состояния сервиса"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': Config.APP_NAME
    })

@app.route('/receive', methods=['POST'])
def receive_request():
    """Основной эндпоинт для приёма запросов"""
    try:
        # Получаем данные из запроса
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()
        
        # Логируем входящий запрос
        request_info = {
            'timestamp': datetime.now().isoformat(),
            'method': request.method,
            'headers': dict(request.headers),
            'remote_addr': request.remote_addr,
            'user_agent': request.headers.get('User-Agent'),
            'data': data
        }
        
        logger.info(f"Received request: {json.dumps(request_info, ensure_ascii=False)}")
        
        # Простая обработка данных
        response_data = {
            'status': 'success',
            'message': 'Request received successfully',
            'timestamp': datetime.now().isoformat(),
            'received_data': data,
            'request_id': f"req_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Error processing request: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/receive', methods=['GET'])
def receive_get():
    """Обработка GET запросов"""
    query_params = request.args.to_dict()
    
    request_info = {
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'headers': dict(request.headers),
        'remote_addr': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'query_params': query_params
    }
    
    logger.info(f"Received GET request: {json.dumps(request_info, ensure_ascii=False)}")
    
    response_data = {
        'status': 'success',
        'message': 'GET request received successfully',
        'timestamp': datetime.now().isoformat(),
        'query_params': query_params,
        'request_id': f"req_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    }
    
    return jsonify(response_data), 200

@app.route('/status', methods=['GET'])
def status():
    """Получение статуса сервиса"""
    return jsonify({
        'status': 'running',
        'timestamp': datetime.now().isoformat(),
        'version': Config.APP_VERSION,
        'environment': Config.FLASK_ENV
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found',
        'timestamp': datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'timestamp': datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    logger.info(f"Starting {Config.APP_NAME} on {Config.HOST}:{Config.PORT}")
    logger.info(f"Environment: {Config.FLASK_ENV}, Debug: {Config.DEBUG}")
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)

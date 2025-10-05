#!/bin/bash
set -e

# Создаем директорию для сертификатов
mkdir -p certs

# Генерируем самоподписанный сертификат
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes \
    -subj "/C=RU/ST=Moscow/L=Moscow/O=Test/OU=Test/CN=localhost"

echo "SSL сертификаты созданы в директории certs/"
echo "Файлы: certs/cert.pem и certs/key.pem"

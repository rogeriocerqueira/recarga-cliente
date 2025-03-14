# Dockerfile (Ponto de Recarga)
FROM python:3.13.2
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "ponto_recarga.py"]

# docker-compose.yml
version: "3.10"
services:
  servidor:
    build: ./nuvem
    ports:
      - "5000:5000"
  ponto:
    build: ./ponto_de_recarga
    ports:
      - "6000:6000"

FROM python:3.13.2
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "servidor.py"]

# Dockerfile para Ponto de Recarga

# Dockerfile (Ponto de Recarga)
FROM python:3.13.2
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "ponto_recarga.py"]
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Installation des dépendances avec gestion des retries
RUN python -m pip install --upgrade pip --retries 10 --timeout 60 && \
    python -m pip install --no-cache-dir --retries 10 --default-timeout=1000 -r requirements.txt

# Copier le reste du projet
COPY . .

EXPOSE 5000

CMD ["python", "-u", "app.py"]

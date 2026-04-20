# 1. Utiliser une image Python légère (Debian slim)
FROM python:3.11-slim

# 2. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 3. Copier d'abord les dépendances (pour optimiser le cache Docker)
COPY requirements.txt .

# 4. Installer les dépendances sans cache (gain de place)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le reste du code source
COPY . .

# 6. Exposer le port de l'application (généralement 5000 pour Flask)
EXPOSE 5000

# 7. Commande pour lancer l'application
CMD ["python", "app.py"]

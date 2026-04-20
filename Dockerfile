# Utilisation d'une image Python légère
FROM python:3.11-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des dépendances en premier pour optimiser le cache
COPY requirements.txt .

# Installation des bibliothèques
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste du code (app.py, templates, static)
COPY . .

# Exposer le port interne de l'application
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]# 1. Utiliser une image Python légère (Debian slim)
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

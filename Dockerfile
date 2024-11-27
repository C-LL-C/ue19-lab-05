# Utiliser une image officielle de Python comme image de base
FROM python:3.11

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances depuis requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet dans le conteneur
COPY . .

# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["python", "app.py"]


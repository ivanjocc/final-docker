# Utiliser une image de base Python
FROM python:3.9-bullseye

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Installer Ollama CLI (remplacez par la version actuelle si nécessaire)
RUN curl -fsSL https://ollama.ai/install.sh | bash

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port par défaut d'Ollama
EXPOSE 11434

# Commande pour démarrer Ollama et le chatbot
CMD ["bash", "-c", "ollama serve & python app.py"]

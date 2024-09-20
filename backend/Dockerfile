# Utiliser une image de base Ubuntu
FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail
WORKDIR /workspaces

COPY requirements.txt .

# Ajouter un utilisateur non-root et définir les permissions
RUN useradd -ms /bin/bash myuser
RUN chown -R myuser:myuser /workspaces

# Passer à l'utilisateur non-root
USER myuser

# Copier les fichiers de l'application et installer les dépendances
# COPY --chown=myuser:myuser . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exposer le port 8000 pour le serveur web
EXPOSE 8000

COPY . .


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1

# Définir le répertoire de travail
WORKDIR /app

COPY requirements.txt .

# Mise à jour de pip et installation des dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# user non root + permission
RUN useradd -ms /bin/bash myuser
RUN chown -R myuser:myuser /app

# passer à l'utilisateur non-root
USER myuser

COPY --chown=myuser:myuser . .

# Exposer le port 8000 pour le serveur web
EXPOSE 8000


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

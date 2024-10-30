FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# user non root + permission
RUN useradd -ms /bin/bash myuser 
RUN chown -R myuser:myuser /app

# passer à l'utilisateur non-root
USER myuser

COPY --chown=myuser:myuser . .

CMD ["python", "bot.py"]
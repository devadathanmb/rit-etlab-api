FROM python:3.11.3-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV FLASK_ENV=production

CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app"]

FROM python:3.10.6
WORKDIR /app

COPY requirements.txt app.py text_processing.py .flaskenv ./
RUN pip install -r requirements.txt
ENV FLASK_ENV production

EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "app:app"]


FROM python:3.9-slim-buster

RUN mkdir "app"

WORKDIR /app

COPY . /app

RUN pip3 install flask

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
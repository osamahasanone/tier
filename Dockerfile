FROM python:3.8.11-alpine3.14
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apk add --no-cache mariadb-dev build-base
RUN apk add --no-cache bash
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
# CMD python manage.py runserver 0.0.0.0:8000
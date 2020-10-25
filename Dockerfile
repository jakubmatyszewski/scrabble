FROM python:3.8-slim

COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc
RUN pip install -r requirements.txt
CMD ["python3", "wsgi.py"]
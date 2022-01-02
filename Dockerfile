FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5005

CMD python3 main.py
FROM python:3.8-alpine

COPY . /app/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR /app

CMD python main.py
FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt && python3 manage.py csu

COPY . .

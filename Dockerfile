FROM python:3.6

#RUN pip3 install pip==9.0.3

# App directory
RUN mkdir /app
WORKDIR /app

COPY       . /app
WORKDIR    /app
RUN        pip install pipenv
RUN        pipenv install --system
ENV        SHELL=/bin/bash

CMD        ["python", "/app/toots.py"]

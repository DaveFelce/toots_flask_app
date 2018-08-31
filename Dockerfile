FROM python:3.6

#RUN pip3 install pip==9.0.3
#
## App directory
#RUN mkdir /app
#WORKDIR /app
#
#COPY       . /app
#WORKDIR    /app
#RUN        pipenv install
#ENV        SHELL=/bin/bash
#ENTRYPOINT ["pipenv", "run"]
CMD        ["python"]
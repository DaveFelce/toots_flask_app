FROM       python
# -- Install Pipenv:
RUN apt update && apt install python3-pip git -y && pip3 install pipenv
COPY       . /app
WORKDIR    /app
RUN        pipenv install
ENV        SHELL=/bin/bash
ENTRYPOINT ["pipenv", "run"]
CMD        ["python"]
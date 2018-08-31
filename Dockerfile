FROM       python
RUN        pip install --upgrade pip==9.0.3
RUN        pip install pipenv
COPY       . /app
WORKDIR    /app
RUN        pipenv install
ENV        SHELL=/bin/bash
ENTRYPOINT ["pipenv", "run"]
CMD        ["python"]
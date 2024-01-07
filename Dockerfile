FROM python:3.10-slim
ARG REPO

RUN pip3 install --upgrade pip

RUN pip3 install poetry

WORKDIR /opt/minimal_devsecops_example
ENV REPO=$REPO

COPY . .
RUN poetry install --no-root --sync

ENTRYPOINT ["poetry", "run", "flask", "--app", "main", "run", "--host=0.0.0.0"]

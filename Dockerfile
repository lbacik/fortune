FROM python:3.7

ENV FORTUNES=/usr/share/games/fortunes
ENV PYTHONPATH=src

RUN apt-get -y update && apt-get -y install \
    fortune \
    fortunes

COPY . /opt/project
WORKDIR /opt/project

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "lfortune.cli.cli"]

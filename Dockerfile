FROM python:3.7

ENV FORTUNES=/usr/share/games/fortunes

RUN apt-get -y update && apt-get -y install \
    fortune

COPY . /opt/project
WORKDIR /opt/project

RUN pip install -r requirements.txt

EXPOSE 5000

CMD uwsgi --ini config.ini

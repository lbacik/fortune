FROM python:3.7

COPY . /opt/project
WORKDIR /opt/project

RUN pip install -r requirements.txt

EXPOSE 5000

CMD uwsgi --ini config.ini

# pythonのバージョンは任意
FROM python:3.8

WORKDIR /usr/src
ENV FLASK_APP=runserver

COPY requirements.txt /user/src/

RUN pip install --upgrade pip
RUN pip install -r /user/src/requirements.txt

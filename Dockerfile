FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /data
WORKDIR /data
ADD requirements.txt /data/
RUN pip3 install -r requirements.txt
ADD . /data/

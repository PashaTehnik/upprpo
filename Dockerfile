FROM python:3.10.4-alpine

MAINTAINER Pavel Polovinko, Vasiliy Babushkin, Ekaterina Korneeva

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /upprpo

COPY ./* /upprpo/

WORKDIR /upprpo

RUN adduser -D user

USER user



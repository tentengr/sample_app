FROM python:3.7.6-alpine3.11

WORKDIR /app

RUN apk add --virtual \
	pip_install_depedencies git gcc linux-headers musl-dev openssl-dev libffi-dev;

RUN pip install --user cookiecutter

ENV PATH="/root/.local/bin:${PATH}"

VOLUME /app

CMD /bin/sh
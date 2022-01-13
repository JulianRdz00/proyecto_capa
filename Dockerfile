FROM python:3.9.5-slim-buster as base

ENV PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off

WORKDIR /app

RUN set -ex \
  && ln -sf /usr/share/zoneinfo/America/Buenos_Aires /etc/timezone \
  && ln -sf /usr/share/zoneinfo/America/Buenos_Aires /etc/localtime \
  && BUILD_DEPS="build-essential python-dev python3-dev libevent-dev python3-pip curl libpq-dev gcc musl-dev postgresql python-psycopg2 libpq5" \
  && apt-get update && apt-get -y --no-install-recommends install $BUILD_DEPS make \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
  && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

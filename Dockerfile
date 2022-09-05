FROM python:3.10

ENV POETRY_VERSION=1.1.14
ENV TELEGRAM_API_TOKEN=""
ENV PYTHONPATH "${PYTHONPATH}:/app"
ARG ENV

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /app/

RUN apt-get update \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false


COPY bot/ /app/bot
COPY bot/ /app/migrations
WORKDIR /app/

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
COPY alembic.ini alembic.ini

RUN poetry install --no-root $(if test "$ENV" = prod; then echo "--no-dev"; fi)

CMD ["python", "bot/main.py"]

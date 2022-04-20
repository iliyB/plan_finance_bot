FROM python:3.9

ENV POETRY_VERSION=1.1.12
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

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
COPY alembic.ini alembic.ini

RUN poetry install $(if test "$ENV" = prod; then echo "--no-dev"; fi)
COPY bot/ /app/bot
WORKDIR /app/

CMD ["uvicorn", "bot.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

#ENTRYPOINT ["python", "bot/main.py"]
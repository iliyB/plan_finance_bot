build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

precommit-install:
	pip3 install pre-commit
	pre-commit install

lint:
	pre-commit run --all-files

makemigrations:
	docker-compose run --rm bot alembic revision --autogenerate -m "$(name)"

migrate:
	docker-compose run --rm bot alembic upgrade head

downgrade:
	docker-compose run --rm bot alembic downgrade -1

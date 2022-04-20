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

path:
	docker-compose run --rm --no-deps bot_app ls
	docker-compose run --rm --no-deps bot_app pwd
	docker-compose run --rm --no-deps bot_app ls app

makemigrations:
	alembic revision --autogenerate -m "$(name)"

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1

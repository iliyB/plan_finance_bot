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
	alembic revision --autogenerate -m "$(name)"

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1

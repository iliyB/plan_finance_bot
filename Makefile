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

# makemigrations:
# # 	docker-compose exec bot -- alembic -c alembic.ini revision --autogenerate -m "$(m)"
# 	alembic -c src/app/alembic.ini revision --autogenerate -m "$(m)"
# #     docker-compose run --rm --no-deps bot alembic revision -m "$(name)"
#
# migrate:
# 	PYTHONPATH=$(shell pwd):${PYTHONPATH} poetry run alembic upgrade head
#
# migration:
# 	PYTHONPATH=$(shell pwd):${PYTHONPATH} poetry run alembic revision --autogenerate -m "${message}"
#
# downgrade:
# 	PYTHONPATH=$(shell pwd):${PYTHONPATH} poetry run alembic downgrade -1
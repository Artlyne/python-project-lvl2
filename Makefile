# Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r gendiff

lint:
	poetry run flake8 gendiff

run:
	poetry run gendiff -h

# Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r gendiff

run:
	poetry run gendiff -h

# Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r diff_calc

run:
	poetry run gendiff -h

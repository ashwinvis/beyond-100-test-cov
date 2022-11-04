test_v1:
	pytest --cov="swedish_cities_v1" --cov-report=term-missing tests/$@.py

test_v2:
	pytest --cov="swedish_cities_v2" --cov-report=term-missing tests/$@.py

.PHONY: tests
tests:
	pytest --cov --cov-report=term-missing

types:
	mypy --ignore-missing-imports src tests

cli_v1:
	python -m swedish_cities_v1

cli_v2:
	python -m swedish_cities_v2 "year >= 1500" "year < 1600"

cli_v2_typed:
	python -m swedish_cities_v2_typed "year >= 1500" "year < 1600"

requirements: requirements.in self.txt
	pip-compile
	pip-sync requirements.txt self.txt

format:
	black src tests
	isort src tests


.PHONY: test

TEST = test
SRC  = google_foobar

install:
	pip install -r requirements.txt
	pre-commit install

test:
	pytest test

coverage:
	coverage run --source $(SRC) -m pytest $(TEST)
	coverage report --show-missing --fail-under 100

format:
	isort --recursive $(SRC) $(TEST)
	black $(SRC) $(TEST)

hooks:
	pre-commit run --all-files

test-build: hooks coverage

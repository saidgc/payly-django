files = `find . -name '*.py' -not -path './.*'`
cov_args = --include 'service/*'

typecheck:
	mypy --non-interactive --install-types .

format:
	- add-trailing-comma $(files)
	- pyformat -i $(files)
	isort -rc $(files)

lint:
	flake8 $(files)

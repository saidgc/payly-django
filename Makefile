files = `find service tests -name '*.py'`
cov_args = --include 'service/*'
FILE=

format:
	- add-trailing-comma $(files)
	- pyformat -i $(files)
	isort -rc $(files)

typecheck:
	mypy --non-interactive --install-types service

lint:
	flake8 service tests
	make typecheck

mi:
	radon mi -e "node_modules/*" service

cc:
	radon cc -e "node_modules/*" service

test:
	if [ -z "${FILE}" ]; then  \
		PYTHONPATH=":." mamba tests --format documentation --enable-coverage && make cov; \
	else \
		PYTHONPATH=":." mamba $(FILE) --format documentation; \
	fi
cov:
	coverage report -m $(cov_args)

htmlcov:
	coverage html $(cov_args)

xmlcov:
	coverage xml $(cov_args)

venv:
	PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev

commit_check:
	cz check --rev-range origin/master..HEAD

bump:
	cz bump --changelog --yes

dev:
	pip install -e '.[dev]'

test:
	pytest
	pycodestyle .

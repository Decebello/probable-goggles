venv:
	python -m venv .venv

install: venv
	.venv\Scripts\pip install -r requirements.txt
	.venv\Scripts\pip install -e .

test:
	.venv\Scripts\pytest tests/

lint:
	.venv\Scripts\flake8 src/ tests/

typecheck:
	.venv\Scripts\mypy src/

docs:
	python -m pydoc -w ndfl.calculator

docs:
	python -m pydoc -w ndfl.calculator
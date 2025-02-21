# Define variables
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
TWINE := $(VENV)/bin/twine

# Create virtual environment
.PHONY: create-venv
create-venv:
	rm -rf $(VENV)
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel build twine
	$(PIP) install .[dev]


# Build the package (Using build module)
.PHONY: build
build:
	rm -rf dist/
	$(PYTHON) -m build

# Upload to PyPI
.PHONY: upload
upload: build
	$(TWINE) upload dist/* --verbose

# Run all tests
.PHONY: test
test:
	 pytest --maxfail=1 --disable-warnings --cov=bababel --cov-report=term-missing:skip-covered --cov-fail-under=90 --color=yes --durations=10

.PHONY: clean
clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info .pytest_cache .coverage
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.log" -delete

.PHONY: code-convention
code-convention:
	pre-commit run --all-files

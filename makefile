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

# Upload to TestPyPI
.PHONY: upload-test
upload-test: build
	$(TWINE) upload --repository testpypi dist/* --verbose
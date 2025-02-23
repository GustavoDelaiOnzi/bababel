# Define variables
VERSION := 3.13.2
PROJECT:= bababel
VENV := $(PROJECT)-$(VERSION)
PYTHON_BIN = $(shell pyenv root)/versions/$(VENV)/bin
TWINE := $(PYTHON_BIN)/bin/twine
PIP = $(PYTHON_BIN)/pip

# Create virtual environment
.PHONY: create-venv
create-venv:
	pyenv install -s $(VERSION)
	pyenv uninstall -f $(VENV)
	pyenv virtualenv $(VERSION) $(VENV)
	$(PIP) install --upgrade pip
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

.PHONY: code-convention
run-rabbit:
	@docker start rabbitmq 2>/dev/null || docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

c:
	cz ch
	git add CHANGELOG.md
	# Count the number of added lines
	ADDED_LINES=$(git diff --cached --numstat | awk '{print $1}' | paste -sd+ - | bc); \
	if [ "$$ADDED_LINES" -eq 1 ]; then \
		git commit --amend --no-edit; \
		echo "✅ Commit amended with 1 added line."; \
	else \
		echo "❌ Commit blocked! Only one line addition is allowed."; \
		exit 1; \
	fi

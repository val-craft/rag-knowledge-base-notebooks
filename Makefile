# Variables
VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python

.PHONY: start jupyter lab
run:
	@echo "Running the Jupyter Lab application..."
	uv run jupyter lab
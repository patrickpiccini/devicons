#!make
VENV=PY31
PYTHON = $(VENV)/bin/python3.11
PIP = $(VENV)/bin/pip

run_main:
	$(PYTHON) -m main.py



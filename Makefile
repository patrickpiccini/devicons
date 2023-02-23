#!make
VENV=PY31
PYTHON = $(VENV)/bin/python3.11
PIP = $(VENV)/bin/pip

default: run_api

run_main:
	$(PYTHON) -m main.py

run_api:
	$(PYTHON) -m I-con\src\api\api.py

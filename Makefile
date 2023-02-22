#!make

export PYTHON=python

default: run_api

run_main:
	$(PYTHON) -m main.py

run_api:
	$(PYTHON) -m I-con\src\api\api.py

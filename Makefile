#!make

export PYTHON=python

default: run_api

run_api:
	$(PYTHON) -m main.pt

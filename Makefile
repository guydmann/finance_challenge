.ONESHELL:

.PHONY: install collect_data run all

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;


collect_data:
	. venv/bin/activate; \
	python collect_data.py

run:
	. venv/bin/activate; \
	python calculate_data.py

all: install collect_data run
install:
	virtualenv venv --python=python3; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; \

flake8:
	. venv/bin/activate; \
	flake8 --exclude=venv --max-line-length=120; \

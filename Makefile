install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; \

flake8:
	. venv/bin/activate; \
	flake8 --exclude=venv --max-line-length=120; \

tests:
	. venv/bin/activate; \
	./manage.py test

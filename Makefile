.PHONY: help dev migrate migrations shell superuser test install clean

# Detect python executable
ifeq ($(OS),Windows_NT)
    PYTHON = env/Scripts/python
    PIP = env/Scripts/pip
else
    PYTHON = env/bin/python
    PIP = env/bin/pip
endif

help:
	@echo "Available commands:"
	@echo "  make dev          - Run Django development server"
	@echo "  make migrations   - Create new database migrations"
	@echo "  make migrate      - Run database migrations"
	@echo "  make shell        - Open Django shell (with shell_plus auto-imports)"
	@echo "  make superuser    - Create a Django superuser"
	@echo "  make test         - Run tests"
	@echo "  make install      - Install dependencies from requirements.txt"
	@echo "  make clean        - Clean pycache and staticfiles"

dev:
	$(PYTHON) manage.py runserver

migrations:
	$(PYTHON) manage.py makemigrations

migrate:
	$(PYTHON) manage.py migrate

shell:
	$(PYTHON) manage.py shell_plus

superuser:
	$(PYTHON) manage.py createsuperuser

test:
	$(PYTHON) manage.py test

install:
	$(PIP) install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

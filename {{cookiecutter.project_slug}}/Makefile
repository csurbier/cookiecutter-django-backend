.PHONY: help install migrate runserver shell test clean

help:
	@echo "Commandes disponibles:"
	@echo "  make install      - Installer les dépendances"
	@echo "  make migrate      - Appliquer les migrations"
	@echo "  make runserver    - Démarrer le serveur de développement"
	@echo "  make shell        - Ouvrir un shell Django"
	@echo "  make test         - Lancer les tests"
	@echo "  make clean        - Nettoyer les fichiers temporaires"
{% if cookiecutter.use_celery == "yes" %}
	@echo "  make celery       - Démarrer le worker Celery"
	@echo "  make celerybeat   - Démarrer Celery Beat"
{% endif %}

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

runserver:
	python manage.py runserver

shell:
	python manage.py shell

test:
	pytest

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete

{% if cookiecutter.use_celery == "yes" %}
celery:
	celery -A {{ cookiecutter.project_slug }} worker -l info

celerybeat:
	celery -A {{ cookiecutter.project_slug }} beat -l info
{% endif %}


PORT ?= 7777

dev:
	poetry run ./manage.py runserver $(PORT)

lint:
	poetry run flake8

# use it if you want translate your app
makemessages:
	poetry run ./manage.py makemessages -l ru

compilemessages:
	poetry run ./manage.py compilemessages

makemigrations:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

shell:
	poetry run ./manage.py shell

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

fill_db_test_data:
	poetry run ./manage.py create_test_users
	poetry run ./manage.py create_test_checking_accounts
	poetry run ./manage.py create_test_payment_requests

prod: migrate fill_db_test_data start

test:
	poetry run ./manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml


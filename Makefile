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
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) __project__.wsgi:application

DEFAULT_AMOUNT_FOR_TEST_OBJECTS = 50
fill_db_test_data:
	poetry run ./manage.py create_test_users $(DEFAULT_AMOUNT_FOR_TEST_OBJECTS)
	poetry run ./manage.py create_test_checking_accounts $(DEFAULT_AMOUNT_FOR_TEST_OBJECTS)
	poetry run ./manage.py create_test_payment_requests $(DEFAULT_AMOUNT_FOR_TEST_OBJECTS) $(DEFAULT_AMOUNT_FOR_TEST_OBJECTS)

prod: migrate start

test:
	poetry run ./manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml


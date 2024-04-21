make:
	cd backend && python manage.py makemigrations
mig:
	cd backend && python manage.py migrate

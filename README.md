# LittleLemon
Meta Django backend developer Capstone
Little Lemon Restaurant - Back-End Capstone Project
====================================================

Prerequisites
-------------
- Python 3.13
- MySQL
- Pipenv
- Insomnia REST client

Setup Instructions
------------------
1. Clone the repository
   git clone <repo_url>
   cd Littlelemon

2. Install dependencies
   pipenv install

3. Activate the virtual environment
   pipenv shell

4. Create MySQL database
   Log into MySQL and run:
   CREATE DATABASE littlelemon;

5. Configure database in settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'littlelemon',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

6. Run migrations
   python manage.py migrate

7. Create a superuser
   python manage.py createsuperuser

8. Run the server
   python manage.py runserver

Browse the Application
-----------------------
Home:         http://localhost:8000/restaurant/
Menu:         http://localhost:8000/restaurant/menu/
Reservations: http://localhost:8000/restaurant/reservations/
Admin Panel:  http://localhost:8000/admin/

Testing the API with Insomnia
------------------------------
Step 1 - Register a new user
   POST http://localhost:8000/auth/users/
   Body (JSON):
   {
       "username": "newuser",
       "password": "yourpassword"
   }

Step 2 - Get your token
   POST http://localhost:8000/restaurant/api-token-auth/
   Body (JSON):
   {
       "username": "newuser",
       "password": "yourpassword"
   }
   Copy the token from the response.

Step 3 - Add Authorization header for secured endpoints
   In Insomnia, go to the Headers tab and add:
   Key:   Authorization
   Value: Token <your_token>

Step 4 - Get all menu items (no auth required)
   GET http://localhost:8000/restaurant/api/menu/

Step 5 - Create a menu item (no auth required)
   POST http://localhost:8000/restaurant/api/menu/
   Body (JSON):
   {
       "title": "Bruschetta",
       "price": "8.99",
       "inventory": 50
   }

Step 6 - Get all bookings (auth required)
   GET http://localhost:8000/restaurant/api/bookings/

Step 7 - Create a booking (auth required)
   POST http://localhost:8000/restaurant/api/bookings/
   Body (JSON):
   {
       "first_name": "John",
       "reservation_date": "2026-04-10",
       "reservation_slot": 12
   }

Step 8 - Update a booking (auth required)
   PUT http://localhost:8000/restaurant/api/bookings/<id>/
   Body (JSON):
   {
       "first_name": "Jane",
       "reservation_date": "2026-04-10",
       "reservation_slot": 14
   }

Step 9 - Delete a booking (auth required)
   DELETE http://localhost:8000/restaurant/api/bookings/<id>/

Running Unit Tests
------------------
   python manage.py test restaurant

Expected output:
   Found 2 test(s).
   OK
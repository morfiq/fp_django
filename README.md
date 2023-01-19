Project: Django website to upload json file and then display in a table
About:
Django project to upload json file from a web page and store data in PostgreSQL database, display the same data in tabular
format for logged in user. User registration and authentication also supported.

Steps to run the application:
pip install django
pip install djangorestframework

Prerequisites:
1. Install postgresql server
2. Install pgadmin or any client for validations

Steps:
Once source code is copied, please use below commands to run the server.

1. update database details in setting.py
2. <python manage.py make migrations>
3. <python manage.py make migrate>
4. <python manage.py runserver?
5. webserver will be up and running on below link
http://127.0.0.1:8000/

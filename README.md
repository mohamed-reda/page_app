##

pipenv install django~=3.1.14

~= which will ensure security updates for Django, such as 3.1.1, 3.1.2, and so on.

------------------------------------------------------------------------------

check

django-admin --version

------------------------------------------------------------------------------

activate virtual environment:

pipenv shell

------------------------------------------------------------------------------

if this runs with no error:

django-admin startproject config .

so my virtual environment has Django installed properly.

here without (.) to the command, it will create config folder in config folder


------------------------------------------------------------------------------

running Django’s local web server python manage.py runserver

exit

------------------------------------------------------------------------------

pipenv shell

exit

------------------------------------------------------------------------------

python manage.py migrate python manage.py startapp pages

• admin.py is a configuration file for the built-in Django Admin app

• apps.py is a configuration file for the app itself

• migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync

• models.py is where we define our database models which Django automatically translates into database tables

• tests.py is for our app-specific tests

• views.py is where we handle the request/response logic for our web app

------------------------------------------------------------------------------
Run:

python manage.py runserver

------------------------------------------------------------------------------
test:

python manage.py test

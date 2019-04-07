
CREAR ENTORNO VIRTUAL

$ pipenv shell
------------------------------------------------------------------

INTASLAR DJANGO

$ pipenv install django djangorestframework django-rest-knox
------------------------------------------------------------------

INICIAR PROYECTO

$ django-admin startproject leadmanager
------------------------------------------------------------------

INICIAR APP

$ python manage.py startapp leads
------------------------------------------------------------------

INCLUIR EN EL LEADMAGANER/SETTING 

INSTALLED_APPS = [
	---,
	---,
	'leads',
	'rest_frame'
     ]

------------------------------------------------------------------

CREAR MIGRACIONES

python manage.py makemigrations leads
------------------------------------------------------------------
EJECUTAR MIGRACIONES

python manage.py migrate
------------------------------------------------------------------

CORRER SERVIDOR

python manage.py runserver

------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------



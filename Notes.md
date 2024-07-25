# Django

## Commands to setup
<!-- - py -m venv .venv -->
- pip install uv
- uv venv   -- create a virtual environment at venv
- .venv\Scripts\activate    -- to run activate file
- deactivate    -- to deactivate the virtual environment
- uv pip install Django
- django-admin startproject projectWithDjango       -- to setup the project
- cd projectWithDjango
- python manage.py runserver (portNumber, by default = 8000)     -- to run the project
- python manage.py startapp django_app      -- to create an app project


## tailwind configuration
- uv pip install django-tailwind
- uv pip install 'django-tailwind[relaod]'      -- giving problems, so we need to do this with pip only

- python -m ensurepip --upgrade     (70 - 80% chances, that it will get installed)
- python -m pip install --upgrade pip       -- not wotking in my system
- pip install 'django-tailwind[relaod]'  

Requirement already satisfied: django-tailwind[relaod] in c:\python\lib\site-packages (3.8.0)
WARNING: django-tailwind 3.8.0 does not provide the extra 'relaod'

- in settings.py --> add tailwind in installed apps
- python manage.py tailwind init
add the theme app in the settings.py now

- NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd" (in settings.py)
- python manage.py tailwind install

- python manage.py tailwind start  (in another terminal)


- python manage.py tailwind build  (for production grade and not for development)



## migrations
- python manage.py migrate

## super user command
- python manage.py createsuperuser
- python manage.py changepassword Khushi (username here for changing the password)


- python -m pip install Pillow


## commands for there changes in the database
- python manage.py makemigrations django_app
- python manage.py migrate


## documentation
https://docs.chaicode.com/
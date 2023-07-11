# Project setup
Installed extension Python from Microsoft.  
Created project folder.  
Created virtual environment: View > Command Palette or (Ctrl+Shift+P). Then select the Python: Select Interpreter command.  
Installed Django.  
Started project: django-admin startproject quotes .  
Added docutils path to project urls, settings INSTALLED_APPS and MIDDLEWARE.  
Installed admindoc: pip install docutils  
Create user: python manage.py createsuperuser  
Installed psycopg2.  

# Start app  
python manage.py startapp appname  
Register app in project settings INSTALLED_APPS.  
Create migration for the model item:  
python manage.py makemigrations    - may also add app name to the end
Create db:  
python manage.py migrate

# Run the project  
python manage.py runserver
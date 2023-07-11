# Project setup
Installed extension Python from Microsoft.  
Created project folder and .py file.  
Created virtual environment: View > Command Palette or (Ctrl+Shift+P). Then select the Python: Select Interpreter command:  
Installed Django: pip install django.  
Started project: django-admin startproject quotes .  
Added docutils path to project urls, settings INSTALLED_APPS and MIDDLEWARE.  
Installed admindoc: pip install docutils  
Create user: python manage.py createsuperuser

# Start app  
python manage.py startapp appname  
Register app in project settings INSTALLED_APPS.  
Created tables: python manage.py migrate  

# Run the project  
python manage.py runserver
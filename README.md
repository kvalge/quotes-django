# Quotes Application  
A web app to display and manage quotes of famous persons.  

Framework: Django.  

Used IDE: Visual Studio Code.  
Database: PostgreSQL.  

# Project setup  
Installed extension Python from Microsoft.  
Created virtual environment: View > Command Palette or (Ctrl+Shift+P) - Select Interpreter command.  
Installed Django.  
Started project: django-admin startproject quotes .  
Created app: python manage.py startapp appname  
Registered app in project settings INSTALLED_APPS.  
Added docutils path to project urls, settings INSTALLED_APPS and MIDDLEWARE.  
Installed admindoc: pip install docutils  
Created user: python manage.py createsuperuser  
Installed psycopg2.  

# Start app  
Created migration for the model:  
python manage.py makemigrations    
Created db:  
python manage.py migrate  

# Run the project  
python manage.py runserver  

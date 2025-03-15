# Django - creating API - Fixtures 

## About
This repository is my eighteenth homework assignment from the Python Pro course. This is my first introduction to the Django framework.
I will make web-site that calls pet-shelter. Tha main idea for this site is to allow users to schedule visits with animals in a shelter. 
The platform enables potential adopters to browse available pets and book appointments to meet them in person.

Main task in this repo is to add fixtures to the apps test.py and implement Docker.
Fixtures in Django are used to preload database data for testing and initialization. 
Export data with dumpdata, import with loaddata, and use them in tests via the fixtures attribute. 
Formats: JSON, XML, YAML.

Added some functional to the apps, like:
- Adedd fixtures to the apps test.py
- Created all_data.json fixture
- Added Dockerfile and docker-compose.yml
- Switched db to postgreSQL

## Run API
1. Clone the repository:  
   ```bash
   git clone https://github.com/OleksiiUzu/django-api-homework-18-fixtures-docker.git
   cd django-api-homework-18-fixtures-docker
2.(Optional) Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate

3.Install dependencies:
  pip install -r requirements.txt

4.run command:
    python manage.py runserver

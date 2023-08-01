# Project: Django REST Framework and Docker + SimpleJWT, Gunicorn & Whitenoise

##### Author: Araceli García


### Links and Resources

Using Django REST framework to create an API, then containerize it with Docker.

Using SimpleJWT (JSON Web Tokens) for authentication and authorization, Gunicorn to deploy the web application and 
Whitenoise to enhance the performance and reliability of serving static assets like CSS, JavaScript, images, and other 
files in production environments.

### Features

    - Rebuild a custom version of Things API demo. 
    - Replace with your own application and model.
    - Containerize with Docker.
    - Implement JWT, Gunicorn & Whitenoise

### Setup

**Initiate a virtual environment**

    - python3.11 -m venv .venv
    - source .venv/bin/activate

**Run this app**

    - docker compose up

**Endpoint to access the url**

    -/api/v1/cities

**To add cities create a user running the below command**

    - docker compose run web python manage.py createsuperuser


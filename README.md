# IELTSWays Back-end service

### Online IELTS Mock tests platform.


[![](https://img.shields.io/badge/python-3.10-orange)](https://www.python.org/)
[![](https://img.shields.io/badge/Django-4.1-green)](https://www.djangoproject.com/)

<br>

![example](https://github.com/nimadorostkar/IELTSWays/blob/main/docs/screenshot.png)

<br>


## How to run

1. Clone this repository

```bash
git https://github.com/nimadorostkar/IELTSWays
```

2. Install dependencies

```bash
pip install -r requirements/requirements.txt 
```

3. Make .env file (use either prod.env.template or dev.env.template to create .env file)

4. Run the following commands to get started (Development)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

5. also you can run tests manually(Development):

```bash
python manage.py test
```

6. Make sure you have Postgredb running (Production)

7. you can run them manually, after the containers spin up, like so:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate   
```

8. Build the image and spin up the two containers

```bash
docker-compose up -d --build
```

and you can use the postman collection added to this repository:
 IELTSWays.postman_collection.json


 enjoy!
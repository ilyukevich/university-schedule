# university-schedule API

#### django 3.2.8
#### drf-yasg 1.20.0
#### djangorestframework 3.12.4
#### pillow 8.4.0

## install:
```git clone https://github.com/ilyukevich/university-schedule.git```

```pip install -r requirements.txt```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py load_data_accounts```

```python manage.py load_data_university```

```python manage.py load_data_schedule```

```python manage.py collectstatic```

```python manage.py runserver```

## authorization (login: password):
```role superuser - [admin@university-schedule.com: admin]```

```role administrator - [administrator@university-schedule.com: administrator]```

```role specialist - [specialist@university-schedule.com: specialist]```

```role lecturer - [lecturer@university-schedule.com: lecturer]```

```role student - [student@university-schedule.com: student]```

```role other - [other@university-schedule.com: other]```

## access to the project:
```http://localhost/ ```

```http://localhost/secureadmin/```

##get student schedule (set email and day):

```http://localhost/api/schedule-request/```

####email: admin@university-schedule.com
####day: Monday

## Swagger:
```http://localhost/swagger/```

## Redoc:
```http://localhost/redoc/```

## DRF:
```http://localhost/api/```

```http://localhost/api/token/ - token```

```http://localhost/api/token/refresh/ - refresh token```

```http://localhost/api/registrations/ - registration```

```http://localhost/api/login/ - login```

```http://localhost/api/logout/ - logout```

```http://localhost/api/reset-password/ - reset password```

```http://localhost/api/schedule-request/ - request schedule for a student```

##TESTS:

1) enter in container django:

```sudo docker exec -it django bash```

2) from container django.

- run tests (all tests of the project will be executed):

```python manage.py test apps``` 

- run application tests 'accounts', 'university', 'schedule'. Example:

```python manage.py test apps/accounts```

```python manage.py test apps/university```

```python manage.py test apps/schedule```

- run test report detail (-v [0,1,2,3]). Example:

```python manage.py test -v 1 apps```

```python manage.py test -v 2 apps```

```python manage.py test -v 2 apps/university```

```python manage.py test -v 2 apps/schedule```

```python manage.py test -v 3 apps/accounts```

# university-schedule


#### Django 3.2.8
#### DRF 3.12.4
#### Pillow 8.4.0

## install
```git clone https://github.com/ilyukevich/university-schedule.git```

```pip install -r requirements.txt```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py load_data_accounts```

```python manage.py load_data_university```

```python manage.py load_data_schedule```

```python manage.py runserver```

### authorization 
- role superuser - [admin@university-schedule.com: admin]
- role administrator - [administrator@university-schedule.com: administrator]
- role specialist - [specialist@university-schedule.com: specialist]
- role lecturer - [lecturer@university-schedule.com: lecturer]
- role student - [student@university-schedule.com: student]
- role other - [other@university-schedule.com: other]

## access
```http://localhost:8000/ ```

```http://localhost:8000/secureadmin```

##get student schedule (set email and day)
#### http://localhost/api/schedule-request/

## Swagger:
#### http://localhost/swagger/

## Redoc:
#### http://localhost/redoc/

## DRF
#### http://localhost/api/
#### http://localhost/api/token/ - token
#### http://localhost/api/token/refresh/ - refresh token
#### http://localhost/api/registrations/ - registration
#### http://localhost/api/login/ - login
#### http://localhost/api/logout/ - logout
#### http://localhost/api/reset-password/ - reset password



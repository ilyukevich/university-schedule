FROM python:3.8.5
RUN mkdir /code
COPY requirements.txt /code
RUN python -m pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
ADD . /code/
#CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
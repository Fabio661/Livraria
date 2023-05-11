FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFRED=1
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 
    
COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
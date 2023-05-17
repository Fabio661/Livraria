# Livraria

Livraria APP  Backend Python curso EBAC

## pré-requisito

```
Python 3.9>
Docker && docker-compose

```

## Quickstart

1. Clone o projeto

   ```shell
   git clone git@github.com:drsantos20/bookstore.git
   ```

2. Rode o projeto na sua maquina:

   ```shell
   python manage.py migrate
   python manage.py runserver
   ```
   
3. Rode o docker:

   ```shell
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

4. Rode os testes dentro do docker:

   ```shell
   docker-compose exec web python manage.py test
   ```



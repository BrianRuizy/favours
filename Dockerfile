FROM python:3.7-alpine

MAINTAINER Brian Ruiz <brianruizy.com>

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /favours

WORKDIR /favours

# install psycopg2 dependencies
RUN apk update

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN python3 -m pip install -r requirements.txt

RUN python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
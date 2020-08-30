FROM python:3.7-alpine

MAINTAINER Brian Ruiz <brianruizy.com>

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /favours

WORKDIR /favours

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
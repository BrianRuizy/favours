FROM python:3.7-alpine

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade pillow

## install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add build-base

EXPOSE 8000

ADD . /favours

WORKDIR /favours

## add and install requirements


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python -m pip install -r requirements.txt

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
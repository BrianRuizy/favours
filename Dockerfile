FROM python:3.7-alpine

## install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add build-base \
    apk add jpeg-dev zlib-dev
    
EXPOSE 8000

ADD . /favours

WORKDIR /favours

## add and install requirements
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# pull official base image
FROM python:3.10.11-alpine3.17

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 and cryptography dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev cargo

# create directory for the sgpm user
RUN mkdir -p /home/pdtic

# create the sgpm user
RUN addgroup -S pdtic && adduser -S pdtic -G pdtic

# create the appropriate directories
ENV HOME=/home/pdtic
ENV APP_HOME=/home/pdtic/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# Install pip
RUN pip install --upgrade pip

# Copy project
COPY . .

#Install dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/pdtic/wheels -r requirements.txt

# install dependencies
RUN apk update && apk add libpq
RUN pip install --no-cache /home/pdtic/wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# chown all the files to the app user
RUN chown -R pdtic:pdtic $APP_HOME

# change to the app user
USER pdtic

# run entrypoint.sh
ENTRYPOINT ["/home/pdtic/web/entrypoint.sh"]

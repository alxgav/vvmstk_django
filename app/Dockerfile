# pull official base image
FROM python:3.9.10-alpine



# set work directory
WORKDIR /app

# create the appropriate directories
ENV HOME=/app
ENV APP_HOME=/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

# copy entrypoint.sh
COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /app/web/entrypoint.sh
# RUN chmod +x /app/web/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["/app/web/entrypoint.sh"]
RUN ["chmod", "+x", "/app/web/entrypoint.sh"]
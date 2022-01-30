#!/usr/bin/env sh

# if [ "$SQL_DATABASE" = "vvmstk_db" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi
# exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --reload
python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"
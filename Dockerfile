FROM python:3.12.7

WORKDIR /app


COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt


COPY . /app

EXPOSE 8003

CMD [ "gunicorn", "--config", "gunicorn_config.py", "event_planner.wsgi:application"]

FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

COPY ./.env.prod /app/.env

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
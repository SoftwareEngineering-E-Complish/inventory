FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

COPY ./start.sh ./start.sh

# TODO: for dev
COPY ./dynamo_setup/ ./dynamo_setup/

RUN chmod +x ./start.sh

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
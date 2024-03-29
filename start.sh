#!/bin/bash
# Add your command here
# For example: python manage.py migrate

# Start the service
sleep 5 # wait for postgres to actually start, otherwise the script will fail
python postgres_setup/create_schema.py
python postgres_setup/insert_test_data.py
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
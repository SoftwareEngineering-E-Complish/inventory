#!/bin/bash
# Add your command here
# For example: python manage.py migrate

# Start the service
python dynamo_setup/create_table.py
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
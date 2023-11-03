#!/bin/bash

# Update pip
echo "Updating pip..."
python pip install -U pip

# Install dependencies

echo "Installing project dependencies..."
python -m pip install -r requirements.txt

echo "Making migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput



echo "Build process completed!"
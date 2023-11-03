python3 pip install -U pip
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

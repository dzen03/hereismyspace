python3 manage.py collectstatic
python3 manage.py compilemessages -l ru --ignore=venv

python3 manage.py check --deploy

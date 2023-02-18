FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 80

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]
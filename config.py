import environ

env = environ.Env()

DEBUG = False
SECRET_KEY = env('SECRET_KEY')
DATABASE_URL = env.db("DATABASE_URL")
import environ

env = environ.Env()

DEBUG = False
try:
    DEBUG = env('DEBUG')
except Exception:
    pass

SECRET_KEY = env('SECRET_KEY')
DATABASE_URL = env.db("DATABASE_URL")

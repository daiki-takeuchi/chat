DEBUG = False
TESTING = False

# CloudSQL & SQLAlchemy configuration
HOST = '146.148.78.74'
PORT = '3306'
USER = 'chat_user'
PASSWORD = 'chat_user'
DATABASE = 'chat_db'
SQLALCHEMY_DATABASE_URI = (
    'mysql://{user}:{password}@{host}:{port}/{database}').format(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'development key'

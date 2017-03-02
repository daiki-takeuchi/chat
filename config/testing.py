import os

DEBUG = False
TESTING = True
WTF_CSRF_ENABLED = False

# CloudSQL & SQLAlchemy configuration
HOST = os.getenv('MYSQL_PORT_3306_TCP_ADDR', 'localhost')
PORT = os.getenv('MYSQL_PORT_3306_TCP_PORT', '3306')
USER = os.getenv('MYSQL_ENV_MYSQL_USER', 'chat_user_test')
PASSWORD = os.getenv('MYSQL_ENV_MYSQL_PASSWORD', 'chat_user_test')
DATABASE = os.getenv('MYSQL_ENV_MYSQL_DATABASE', 'chat_db_test')
SQLALCHEMY_DATABASE_URI = (
    'mysql://{user}:{password}@{host}:{port}/{database}').format(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'testing key'

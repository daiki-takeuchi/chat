DEBUG = False
TESTING = False

# CloudSQL & SQLAlchemy configuration
HOST = 'us-cdbr-iron-east-03.cleardb.net'
PORT = '3306'
USER = 'bc490c93bfba0a'
PASSWORD = 'db4577d5'
DATABASE = 'heroku_2fe043177fc40e6'
SQLALCHEMY_DATABASE_URI = (
    'mysql://{user}:{password}@{host}:{port}/{database}').format(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_RECYCLE = 499
SQLALCHEMY_POOL_TIMEOUT = 20

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'development key'

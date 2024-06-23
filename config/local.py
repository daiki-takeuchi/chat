from dotenv import load_dotenv
import os

# .envファイルをロードします。
# 同じ環境変数名が既に設定されている場合は、値を上書きする
load_dotenv(override=True)

DEBUG = True
TESTING = True

# CloudSQL & SQLAlchemy configuration
HOST = 'db'
PORT = '3306'
USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
DATABASE = os.getenv("MYSQL_DATABASE")
SQLALCHEMY_DATABASE_URI = (
    'mysql://{user}:{password}@{host}:{port}/{database}').format(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'development key'

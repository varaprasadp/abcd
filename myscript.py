import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
'''
import urllib.parse as urlparse
url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.user
password = url.password
host = url.host
port = url.port

con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
'''

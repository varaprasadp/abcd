import psycopg2
import urllib.parse as urlparse
import os
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

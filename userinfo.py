from flask import Flask, render_template, request, url_for
from connection import connect
import urllib.parse as urlparse
import os
import psycopg2
import psycopg2.extras
app = Flask(__name__)

@app.route('/')

@app.route('/newuser')
def new_user():
   return render_template('form.html',msg)

@app.route('/add_data',methods = ['POST', 'GET'])
def add_data():
   if request.method == 'POST':
      try:
         name = request.form['name']
         age = request.form['age']
         gender = request.form['gender']
         cur = con.cursor()
         cur.execute("""INSERT INTO database(name,age,gender) VALUES (%s,%s,%s);""",(name,age,gender) )
         con.commit()
         msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()


@app.route('/data')
def data():
   cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
   cur.execute("select * from database;")
   rows = cur.fetchall();
   return render_template("data.html",rows = rows)

if __name__ == '__main__':
   url = urlparse.urlparse(os.environ['DATABASE_URL'])
   dbname = url.path[1:]
   user = url.username
   password = url.password
   host = url.hostname
   port = url.port
   con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
   con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
   try:
      cur=con.cursor()
   except:
      print('cannot connect')
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS database (name varchar(20), age integer, gender varchar(20));")
   app.run(debug = True, use_reloader = True,host="/localhost",port="5432")
   

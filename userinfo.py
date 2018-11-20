from flask import Flask, render_template, request, url_for
import urllib.parse as urlparse
import os
import psycopg2
import psycopg2.extras
import logging

app = Flask(__name__)


@app.route('/')

@app.route('/new_user')
def new_user():
   cur=con.cursor()
   cur.execute("""CREATE TABLE database (name varchar(20), age integer, gender varchar(20))""")
   return render_template('form.html')

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
         msg = "error in insert operation"
      finally:
         con.close()
         return render_template("result.html",msg = msg)
         


@app.route('/data')
def data():
   cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
   cur.execute("select * from database;")
   rows = cur.fetchall();
   return render_template("data.html",rows = rows)

if __name__ == '__main__':
   con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
   gunicorn_logger = logging.getLogger('gunicorn.error')
   app.logger.addHandler(logging.StreamHandler(sys.stdout))
   app.logger.setLevel(logging.ERROR)
   app.run(debug = True, use_reloader = True)
   

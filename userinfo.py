from flask import Flask, render_template, request, url_for
import urllib.parse as urlparse
import os
import psycopg2
import psycopg2.extras
app = Flask(__name__)

@app.route('/')

@app.route('/newuser')
def new_user():
   return render_template('form.html')

@app.route('/add_data',methods = ['POST', 'GET'])
def add_data():
   if request.method == 'POST':
      try:
         name = request.form['name']
         age = request.form['age']
         gender = request.form['gender']
         cur = con.cursor()
         cur.execute("CREATE TABLE IF NOT EXISTS database (name varchar(20), age integer, gender varchar(20));")
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
   con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
   app.run(debug = True, use_reloader = True)

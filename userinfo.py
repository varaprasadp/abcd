from flask import Flask, render_template, request, url_for
from connection import connect
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
    conn = ("dbname='d4669f4pa3dkk8' user='gwvshgjceutpcf' password='6405b053099f7ae42afde62c180253c7a86cb43d3e134eb5a3366aee4a4ee47d' host='ec2-54-235-156-60.compute-1.amazonaws.com' port='5432'")
    try:
        return psycopg2.connect(conn)
    except:
        print('cannot connect')
   con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS database (name varchar(20), age integer, gender varchar(20));")
   app.run(debug = True, use_reloader = True,host="/localhost",port="5432")
   

from flask import Flask, render_template, request, url_for
import sqlite3 as sql
from connection import connect

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
         
         with sql.connect("database") as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS database(name VARCHAR(20),age INTEGER,gender VARCHAR(10);")
            cur.execute("INSERT INTO database(name,age,gender) VALUES (?,?,?)",(name,age,gender) )
            
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
   con = sql.connect("d10vqpdr1b33rr")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from database")
   
   rows = cur.fetchall();
   return render_template("data.html",rows = rows)

if __name__ == '__main__':
   con=connect()
   app.run(debug = True, use_reloader = True)

from flask import Flask, render_template, request, url_for
from connection import connect
import psychopg2
import psychopg2.extras
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
         con=connect()
         cur = con.cursor()
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
  con=connect()
   cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
   cur.execute("select * from database")
   
   rows = cur.fetchall();
   return render_template("data.html",rows = rows)

if __name__ == '__main__':
   con=connect()
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS database (name varchar(20), age integer, gender varchar(20)")
   app.run(debug = True, use_reloader = True,host="ec2-23-21-201-12.compute-1.amazonaws.com",port="5432")
   

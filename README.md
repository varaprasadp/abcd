#I have used psycopg2 to connect to data base

#in th heroku postgresql data baste is used 

flask
gunicorn
psycopg2
sqlite3
these three are the requirements so these are placed in requirements file

i have used python flask

3 web pages are paced one to insert data as form another to show the result and the last one is to see the result

actully in local runner sqlite 3 is used so i have written 2 connections if we run in local runner sqlite3 connection is used and if we run in heroku we use psycopg2 because it dont support sqlite3

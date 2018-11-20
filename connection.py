import psycopg2
import psycopg2.extras

def connect():
    conn = ("dbname='d4669f4pa3dkk8' user='gwvshgjceutpcf' password='6405b053099f7ae42afde62c180253c7a86cb43d3e134eb5a3366aee4a4ee47d' host='ec2-54-235-156-60.compute-1.amazonaws.com' port='5432'")
    try:
        return psychopg2.connect(conn)
    except:
        print('cannot connect')
    
 

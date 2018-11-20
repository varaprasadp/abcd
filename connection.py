import psychopg2
import psychopg2.extras

def connect():
    conn = ('dbname=database user=gwvshgjceutpcf password = 6405b053099f7ae42afde62c180253c7a86cb43d3e134eb5a3366aee4a4ee47d host= ec2-54-235-156-60.compute-1.amazonaws.com')
    try:
        return psychopg2.connect(conn)
    except:
        print('cannot connect')
    
 

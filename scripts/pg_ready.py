
import socket
import time
import os

MAX_RETRIES = 5
retries = MAX_RETRIES

port = int(os.environ.get('DBPORT'))
host = os.environ.get('DBHOST')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

while retries > 0:
    try:
        s.connect((host, port))
        s.close()
        print("PostgreSQL {} is ready on {}".format(host, port))
        break
    except socket.error as ex:
        print("({}/{}) Wating for PostgreSQL...".format(retries, MAX_RETRIES))
        time.sleep(2)
        retries -= 1
if retries == 0:
     raise Exception("Cannot connect to PostgreSQL on {} and port {}".format(host, port))
     

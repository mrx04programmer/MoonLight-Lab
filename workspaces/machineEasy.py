from flask import Flask
import mysql.connector
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def hello():
    return '|---------------------------------------|'

address = ("0.0.0.0", 21)  # Puerto FTP

server = ThreadedFTPServer(address, FTPHandler)
server.serve_forever()

#  MySQL
config = {
    'user': 'admin',
    'password': 'adm1n',
    'host': 'localhost',
    'database': 'backups',
    'port': 3306 
}

try:
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print('Conectado a MySQL')
        conn.close()
except Error as e:
    print('Error:', e)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) # web

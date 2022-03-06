from crypt import methods
from operator import methodcaller
from flask import Flask, jsonify,request,flash
from flaskext.mysql import MySQL
#from mysql import mysql


app = Flask(__name__)

mysql = MySQL()

# MySql configurations

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pao2930'
app.config['MYSQL_DATABASE_DB'] = 'siet_fe'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/users', methods =['GET'])
def get_users():
    #try:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute('select * from socio')
        rows = cur.fetchall()
        #aca transforma las rows en un formato json
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    #except Exception as e:
        print(e)
    #finally:
    #    cur.close()
    #    conn.close()

@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('select * from socio where id_socio = %s',id)
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp
    #print('aca traigo uno solo')


if __name__ == "__main__":
    app.run(debug=True)
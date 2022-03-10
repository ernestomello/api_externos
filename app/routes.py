from app import app
from crypt import methods
from operator import methodcaller
from flask import Flask, jsonify,request,flash
from flaskext.mysql import MySQL
from flask_httpauth import HTTPBasicAuth
from app.mysql import mysql


basic_auth = HTTPBasicAuth

#@basic_auth.verify_password
#def verify_password(username, password):
#    conn = mysql.connect()
#    cur = conn.cursor()
#    cur.execute('select * from socio')
#    user = cur.fetchall()
    





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
from app import app
from crypt import methods
from operator import methodcaller
from flask import Flask, jsonify,request,flash
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.mysql import mysql
import base64
import os


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    #conn = mysql.connect()
    #cur = conn.cursor()
    #cur.execute('select * from socio')
    #user = cur.fetchall()
    user = {
        "usuario":username,
        "password": password
    }
    if username == "emello" and password == "pao2930":
        return True
    return False
    #return print(user)

@token_auth.verify_token
def verify_token(token):
    if token == "lolita la loca":
        return True
    return False 

@app.route('/token', methods =['GET'])
@basic_auth.login_required
def get_token(expires_in=3600):
    #now = datetime.utcnow()
    #cur = mysql.connect().cursor()
    #cur.execute('select * from socio')
    #rows = cur.fetchall()
    token = base64.b64encode(os.urandom(24)).decode('utf-8')
    #token_expiration = now + timedelta(seconds=expires_in)
    resp = jsonify(token)
    resp.status_code = 200
    return "lolita la loca"#resp
    

@app.route('/users', methods =['GET'])
@token_auth.login_required
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
@token_auth.login_required
def get_user(id):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('select * from socio where id_socio = %s',id)
    rows = cur.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp
    #print('aca traigo uno solo')



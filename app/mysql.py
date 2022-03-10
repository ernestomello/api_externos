from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySql configurations

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pao2930'
app.config['MYSQL_DATABASE_DB'] = 'siet_fe'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
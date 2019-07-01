from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'tranch5_sjr'
app.config['MYSQL_DATABASE_PASSWORD'] = 'modernWater360'
app.config['MYSQL_DATABASE_DB'] = 'tranch5_milb'
app.config['MYSQL_DATABASE_HOST'] = 'steveport.com'
mysql.init_app(app)
@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('select * from affiliates')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
   return jsonify({'myCollection' : r})
if __name__ == '__main__':
    app.run()
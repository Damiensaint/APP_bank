from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_SER'] = 'root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] = 'ussd'
import MySQLdb

#db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="database")


mysql = MySQL(app)


#mysql.init_app(app)


@app.route('/')


def index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data =cur.fetchall()

    cur.close()
    return render_template("index.html",users=data)


@app.route('/insert',methods= ['POST'])
def insert():
    names = request.form['names']
    phone = request.form['phone']
    acc = request.form['acc']
    bank = request.form['bank']
    pin = request.form['pin']

    cur = mysql.connection.cursor()

    cur.execute("INSERT into users(name,phoneNbr,AccNbr,bankname,pin) values (%s,%s,%s,%s,%s)",(names,phone,acc,bank,pin))
    mysql.connection.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)



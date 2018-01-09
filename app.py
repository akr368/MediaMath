from flask import Flask, Response, render_template, request, redirect, url_for
from boto3 import client
import time
import sqlite3
import sqlite3 as sql
from datetime import datetime
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

delay = 0
conn = sqlite3.connect('database.db')
print "Opened database successfully";
conn.execute('CREATE TABLE IF NOT EXISTS info (count INTEGER PRIMARY KEY AUTOINCREMENT, delay REAL, rtime timestamp, ipaddress TEXT, useragent TEXT)')
print "Table created successfully";

def get_client():
    return client(
        's3',
        'us-west-2',
        aws_access_key_id='xxx',
        aws_secret_access_key='xxx'
    )

@app.route('/csv_test')
def csv_test():
   return render_template('csv_test.html')

@app.route('/download/', methods=['GET'])
def download():
    try:
        time.sleep(float(request.args.get('delay')))
        delay = float(request.args.get('delay'))
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO info(delay, rtime, ipaddress, useragent) VALUES (?, ?, ?, ?);", (delay, datetime.now(), request.remote_addr,
            request.headers.get('User-Agent'), ))
            con.commit()
            print cur.execute('SELECT * from info').fetchall();
            print  "Record successfully added"
        s3 = get_client()
        file = s3.get_object(Bucket='csvmediamath', Key='data.csv')
        return Response(
        file['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment; filename=data.csv"}
        )
    except:
        con.rollback()
        print "Error."

@app.route('/report')
def report():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from info")
    rows = cur.fetchall();
    return render_template("report.html", rows=rows)

if __name__ == '__main__':
   app.run(debug = True)

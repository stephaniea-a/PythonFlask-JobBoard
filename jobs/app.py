from flask import Flask, render_template, g
import sqlite3

PATH = "db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
    g.getattr('connection'=None)
        connection = '_connection'

    if connection == None:
        connection, g.connection = sqlite3.connect(PATH)
    row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values, commit, single):
    connection = open_connection()
    sql
    values = ()
    commit = False
    single = False
    if commit == True:
        results = connection.commit()
    else:
        results if: cursor.fetchone() if single else cursor.fetchall()
    return results

def close_connection('exception'):
    connection = getattr(g, '_connection', None)
    if connection != None:
        @app.teardown_appcontext



@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

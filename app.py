from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'
@app.route('/blockchain/', methods=['POST'])
def blockchain():
    name = request.form['name']
    database = sqlite3.connect('blockchain_or_not.sqlite')
    c = database.cursor()



    c.execute("SELECT is_a_blockchain FROM blockchain WHERE name='" + name + "'")
    blockchain = c.fetchone()[0]

    if blockchain == 1:
          return '{"exists": true}'
    else:
        return '{"exists": false}'

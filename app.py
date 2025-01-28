from flask import Flask, request
import sqlite3
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello!'
@app.route('/blockchain/', methods=['POST'])
def blockchain():
    name = request.form['name']
    dATABASE = sqlite3.connect('blockchain_or_not.sqlite')
    c = dATABASE.cursor()



    c.execute("SELECT is_a_blockchain FROM blockchain WHERE name='" + name + "'")
    is_it_really_a_blockchain_or_is_it_not = c.fetchone()[0]

    if is_it_really_a_blockchain_or_is_it_not == 1:
          return '{"exists": true}'
    else:
        return '{"exists": false}'

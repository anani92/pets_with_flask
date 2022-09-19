from flask import Flask, redirect, render_template, request, session
from mysql_connection import connectToMySQL
import datetime

app = Flask(__name__)
secret_key = 'keep this secret'

@app.route('/')
def pets():
  mysql = connectToMySQL('candr_pets')
  print(mysql)
  pets = mysql.query_db('select id, name, created_at, updated_at, type FROM pets')
  return render_template('index.html', all_pets=pets)


@app.route('/add-pet', methods=['POST'])
def add_pet():

  add_pet = "INSERT INTO pets(name, type, created_at, updated_at) VALUES(%(name)s, %(type)s, now(), now());"
  data = {
    'name': request.form['name'],
    'type': request.form['type'],
  }
  db = connectToMySQL('candr_pets')

  db.query_db(add_pet, data)
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)
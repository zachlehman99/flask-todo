from flask import Flask, request, make_response, render_template

import os
import datetime
import psycopg2


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        # DB_NAME
        # DB_USER
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/')
    def index():
        conn = psycopg2.connect("dbname='todo_app'")
        print("We Done it!")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM todos''')
        post = cur.fetchall()
        cur.close()
        conn.close()
        print('Closed')
        return render_template('index.html', post=post)



    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            todo = request.form['todo']
            conn = psycopg2.connect(database = "todo_app")
            cur = conn.cursor()
            cur.execute("INSERT INTO todos (todo,completed) VALUES (%s, %s)", (todo, False))
            conn.commit()
            print('-' * 20)
            print("Sent")
            print('-' * 20)
            cur.close()
            conn.close()
            print('-' * 20)
            print("Closed")
            print('-' * 20)

            return render_template('create.html', todo=todo)
        return render_template('create.html')


    @app.route('/update', methods=['GET', 'POST'])
    def update():
        if request.method == 'POST':
            todo = request.form['todo']
            conn = psycopg2.connect(database = "todo_app")
            cur = conn.cursor()
            cur.execute("UPDATE todos SET completed=(%s) WHERE todo=(%s)", (True, todo))
            conn.commit()
            print('-' * 20)
            print("Sent")
            print('-' * 20)
            cur.close()
            conn.close()
            print('-' * 20)
            print("Closed")
            print('-' * 20)
            return render_template('update.html', todo=todo)
        return render_template('update.html')

    @app.route('/delete', methods=['GET', 'POST'])
    def delete():
        if request.method == 'POST':
            todo = request.form['todo']
            conn = psycopg2.connect(database = "todo_app")
            cur = conn.cursor()
            cur.execute("DELETE FROM todos WHERE todo=(%s)", (todo))
            conn.commit()
            print('-' * 20)
            print("Sent")
            print('-' * 20)
            cur.close()
            conn.close()
            print('-' * 20)
            print("Closed")
            print('-' * 20)
            return render_template('delete.html', todo=todo)
        return render_template('delete.html')

    return app

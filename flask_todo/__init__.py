from flask import Flask, request, make_response, render_template

import os
import datetime
import psycopg2


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
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
        conn.close()
        return render_template('index.html', post=post)



    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            todo = request.form['todo']
            conn = psycopg2.connect(database = "todo_app")
            cur = conn.cursor()
            cur.execute(f''' INSERT INTO todos (todo,completed) VALUES ('{todo}',FALSE);''')
            conn.commit()
            print('-' * 20)
            print("Sent")
            print('-' * 20)
            cur.close()
            conn.close()
            print('-' * 20)
            print("Closed")
            print('-' * 20)

            return render_template('index.html', todo=todo)
        return render_template('create.html')


    @app.route('/update', methods=['GET', 'POST'])
    def update():
        if request.method == 'GET':
            return render_template('update.html')
        elif request.method == 'POST':
            lists = open("todo.txt", "r+")
            todo = request.form['todo']
            reading = lists.read()
            if todo == '':
                lists.close()
                return render_template('update.html')
            else:
                lists = open("todo.txt", "r+")
                file_text = lists.readlines()
                lists.seek(0)
                for i in file_text:
                    if not todo in i:
                        lists.write(i)
                lists.truncate()
                lists.write('Completed '), lists.write(todo), lists.write(' '), lists.write(str(datetime.datetime.now())), lists.write(' '), lists.write('\n')
                lists.close()
        return render_template('update.html', todo=todo)

    return app

from flask import Flask, request, make_response, render_template

import datetime

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
        post = open('todo.txt', 'r+')
        file = post.read()
        post.close()
        return render_template('index.html', post=file)



    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('create.html')
        elif request.method == 'POST':
            lists = open("todo.txt", "a")
            todo = request.form['todo']
            posts = []
            if not todo:
                return 'You need to add a Todo'
            posts.append(lists.write(todo)),
            posts.append(lists.write(' ')), posts.append(lists.write(str(datetime.datetime.now()))), posts.append(lists.write(' ')),
            posts.append(lists.write('Not Completed')),
            posts.append(lists.write('\n'))
            lists.close()


        return render_template('create.html', todo=todo, posts=posts)


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

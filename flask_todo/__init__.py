from flask import Flask, request, make_response, render_template

# import flask_todo.db
import datetime
import psycopg2

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        # Some form of something under this to connect the database
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),

    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/')
    def index():
        try:
            conn = psycopg2.connect("dbname='todo_app'")
            print("We Done it!")
        except:
            print("You have an error")
        cur = conn.cursor()
        cur.execute("SELECT * FROM todos")
        post = cur.fetchall()
        conn.close()
        # post = open('todo.txt', 'r+')
        # file = post.read()
        # post.close()
        return render_template('index.html', post=post)



    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('create.html')
        elif request.method == 'POST':
            try:
                conn = psycopg2.connect("dbname='todo_app'")
                print("We Done it!")
            except:
                print("You have an error")
            # if not todo:
            #     return 'You need to add a Todo'
            # cur = conn.cursor()
            # todo = cur.execute(f'INSERT INTO todos (todo, completed) VALUES ({ todo }, False)')
            # conn.close()
            # lists = open("todo.txt", "a")
            # todo = request.form['todo']
            # posts = []
            #
            # posts.append(lists.write(todo)),
            # posts.append(lists.write(' ')), posts.append(lists.write(str(datetime.datetime.now()))), posts.append(lists.write(' ')),
            # posts.append(lists.write('Not Completed')),
            # posts.append(lists.write('\n'))
            # lists.close()


        return render_template('create.html', todo=todo)


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

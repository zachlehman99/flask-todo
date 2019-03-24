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
        return render_template('index.html')

    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('create.html')
        elif request.method == 'POST':
            lists = open("todos.txt", "a")
            todo = request.form['todo']
            if not todo:
                return 'You need to add a Todo'
            lists.write(todo), lists.write(' '),  lists.write(str(datetime.datetime.now())), lists.write(' '), lists.write('Not Completed'), lists.write('\n')
            lists.close()


        return render_template('create.html', todo=todo)

    @app.route('/update')
    def update():
        return render_template('update.html')

    return app

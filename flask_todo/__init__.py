from flask import Flask, request, make_response, render_template


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

    @app.route('/create')
    def create():
        return render_template('create.html')

    @app.route('/update')
    def update():
        return render_template('update.html')

    return app

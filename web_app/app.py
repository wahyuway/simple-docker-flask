from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='FlaskApp')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='FlaskApp')

    return app
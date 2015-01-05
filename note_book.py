from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route('/')
def home_page():
    return "Hello world"

if __name__ == '__main__':
    app.run()
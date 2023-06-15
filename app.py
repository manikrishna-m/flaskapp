from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/2')
def hello1():
    return 'Hello World!1'

@app.route('/3')
def hello2():
    return 'Hello World!2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
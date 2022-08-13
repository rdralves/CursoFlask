from flask import Flask

app = Flask(__name__)


# URL dinâmica 👇👇👇
@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=""):
    return "<h1>Hello {}</h1>".format(nome)


@app.route('/')
def index():
    return '<h1>Home</h1>'

if __name__ == "__main__":
    app.run(debug=True)

import flask
from flask import Flask

app = Flask(__name__)


# Forma usual de criar rotas
@app.route('/')
def index():
    return "index"


# Outra forma de definir uma rota
def teste():
    return "<p>testando 1</p>"


app.add_url_rule("/teste", "teste", teste)

if __name__ == "__main__":
    app.run(debug=True)

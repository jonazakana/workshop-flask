from flask import Flask #il faudra ajouter une fonction a import, a vous de chercher ;)

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return ...  # Compléter ici


if __name__ == '__main__':
    app.run(debug=True)
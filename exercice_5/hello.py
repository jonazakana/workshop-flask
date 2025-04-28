from flask import Flask

app = Flask(__name__)

users = []

@app.route('/add_user/<name>')
def add_user(name):
    pass #a vous de coder la fonction

@app.route('/users')
def get_users():
    return ... # Compléter ici

if __name__ == '__main__':
    app.run(debug=True)
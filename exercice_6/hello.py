# app.py
from flask import Flask #pensez a l'exercice 3 et 4 et au fiat qu'il y a un template...
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

@app.route('/', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        pass #a completer
    return ... #a completer

if __name__ == '__main__':
    app.run(debug=True)
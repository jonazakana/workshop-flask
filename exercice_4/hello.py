from flask import Flask #ajouter 2 fonctions (spoiler une des deux c'est celle de l'exercice précédent)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if ... == 'POST': #completer le if
        pass #completer ici
    return ... #completer ici

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def hello():
    return render_template("index.html")

eleve_list = [
    {'name': 'Dupont', 'prenom': 'Jean', 'class': '2A'},
    {'name': 'Dupont', 'prenom': 'Jeanne', 'class': 'TG2'},
    {'name': 'Dupont', 'prenom': 'Jeanne', 'class': 'TG2'},
    {'name': 'Marchand', 'prenom': 'Marie', 'class': '2A'}, 
    {'name': 'Martin', 'prenom': 'Adeline', 'class': '1G1'},
    {'name': 'Dupont', 'prenom': 'Lucas', 'class': '2A'}
]

@app.route("/eleves")
def eleves():
    classe = request.args.get('c')
    if classe:
        eleves_selectionnes = [eleve for eleve in eleve_list if eleve['class'] == classe]
    else:
        eleves_selectionnes = []
    #classe = request.args['autre']
    print(classe)
    #return render_template("eleve.html", eleves=eleve_list)
    return render_template("eleve.html", eleves=eleves_selectionnes) 


if __name__== '__main__':
    app.run(debug=True)
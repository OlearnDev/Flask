from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/enreg")
def enreg():
    return render_template("formulaire.html") 

@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        donnees = request.form                      
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        if nom == 'admin' and mdp == '1234':
            return render_template("traitement.html", nom_utilisateur = nom)
        else:
            return render_template("traitement.html")
    else:
        return redirect(url_for('hello'))

if __name__== '__main__':
    app.run(debug=True)
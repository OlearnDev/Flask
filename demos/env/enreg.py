from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/enreg")
def enreg():
    return render_template("formulaire.html")

@app.route("/traitement")
def traitement():
    return render_template("Traitement de données")

if __name__== '__main__':
    app.run(debug=True)
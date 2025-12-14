from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobreNosotros")
def sobre_nosotros():
    return render_template("sobreNosotros.html")

@app.route("/anuncios")
def anuncios():
    return render_template("anuncios.html")

@app.route("/concursos")
def concursos():
    return render_template("concursos.html")

@app.route("/nuevosIngresos")
def nuevos_ingresos():
    return render_template("nuevosIngresos.html")


if __name__ == "__main__":
    app.run(debug=True)
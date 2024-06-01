from flask import Flask
import random

app = Flask(__name__)

lista = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones."
]

@app.route("/")
def inicio():
    return '<a href="/dato">¡Ver un hecho al azar!</a><br><a href="/moneda">¡Lanzar una moneda!</a>'

@app.route("/dato")
def dato():
    fact = random.choice(lista)
    return f"<p>{fact}</p><br><a href='/'>Volver a inicio</a>"

@app.route("/moneda")
def moneda():
    result = random.choice(["Cara", "Cruz"])
    return f"<p>Resultado del lanzamiento: {result}</p><br><a href='/'>Volver a inicio</a>"

if __name__ == "__main__":
    app.run(debug=True)

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def inicio():
    conexion = sqlite3.connect("miportafolio.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM sobremi")
    sobremi = [dict(fila) for fila in cursor.fetchall()]

    cursor.execute("SELECT * FROM estudios")
    estudios = [dict(fila) for fila in cursor.fetchall()]

    cursor.execute("SELECT * FROM intereses")
    intereses = [dict(fila) for fila in cursor.fetchall()]
    
    cursor.execute("SELECT * FROM redes")
    redes = [dict(fila) for fila in cursor.fetchall()]

    conexion.close()

    print(sobremi)
    print(estudios)
    print(intereses)
    print(redes)

    return render_template(
        "portafolio.html",
        sobremi=sobremi,
        estudios=estudios,
        intereses=intereses,
        redes=redes
    )

if __name__ == "__main__":
    app.run(debug=True)

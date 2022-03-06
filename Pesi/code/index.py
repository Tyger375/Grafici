import json
from plotlib import *

def grafico1():
    global data
    with open("./Pesi/code/data.json") as f:
        data = json.loads(f.read())

    x = data["forza"]
    y = data["Lunghezza"]
    #Forza-allungamento
    grafico = Grafico(size=(Vector2D(0, 0), Vector2D(1.5, 11)), title="Grafico")
    grafico.set_xlabel("Forza")
    grafico.set_ylabel("Lunghezza")
    grafico.set_x_interval(0.15)
    grafico.set_y_interval(1)
    grafico.fit(x, y)
    grafico.plot(x, y, "+", size=100)
    #grafico.set_grid(True)
    grafico.save("grafico1")

def grafico2():
    global data
    with open("./Pesi/code/data.json") as f:
        data = json.loads(f.read())

    y = data["forza"]
    x = data["peso"]
    xerr = data["Ep"]
    yerr = data["Ef"]

    grafico = Grafico(size=(Vector2D(0, 0), Vector2D(130, 2)), title="Grafico", xticks=20, yticks=0.5)
    grafico.set_xlabel("Forza")
    grafico.set_ylabel("Lunghezza")
    grafico.fit(x, y)
    grafico.plot(x, y, "xyerrorbars", size=100, errx=xerr, erry=yerr)
    #grafico.set_grid(True)
    grafico.save("grafico2")

grafico2()
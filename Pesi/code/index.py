import json
from plotlib import *

def grafico1(esperimento):
    global data, grafico
    with open("./Pesi/code/data.json") as f:
        data = json.loads(f.read())

    data = data["esperimento" + str(esperimento)]
    x = data["forza"]
    y = data["Lunghezza"]
    #Forza-allungamento
    if esperimento == 1:
        grafico = Grafico(size=(Vector2D(0, 0), Vector2D(1.5, 11)), title="l0 = 7cm")
    else:
        grafico = Grafico(size=(Vector2D(0, 0), Vector2D(1.5, 15)), title="l0 = 9cm")
    grafico.set_xlabel("Forza")
    grafico.set_ylabel("Lunghezza")
    grafico.set_x_interval(0.15)
    grafico.set_y_interval(1)

    arrayx, arrayy = getFitArrayWithStartAndEnd(x, y)

    grafico.fit(arrayx, arrayy)
    grafico.plot(x, y, "+", size=100)
    #grafico.set_grid(True)
    grafico.save(f"./Pesi/results/esperimento{esperimento}/grafico1")

def grafico2(esperimento):
    global data, grafico
    with open("./Pesi/code/data.json") as f:
        data = json.loads(f.read())

    data = data["esperimento" + str(esperimento)]
    y = data["C"]
    x = data["Lunghezza"]
    xerr = data["El"]
    yerr = data["Ec"]

    if esperimento == 1:
        grafico = Grafico(size=(Vector2D(0, 0), Vector2D(15, 15)), title="l0 = 7cm", debug=True)#, xticks=1, yticks=5)
        grafico.set_x_interval(array=np.arange(0, 16, 2))
        grafico.set_y_interval(array=np.arange(0, 16, 2))
    else:
        grafico = Grafico(size=(Vector2D(0, 0), Vector2D(15, 25)), title="l0 = 9cm", debug=True)#, xticks=1, yticks=5)
        grafico.set_x_interval(array=np.arange(0, 16, 2))
        grafico.set_y_interval(array=np.arange(0, 26, 2))
    grafico.set_xlabel("x (cm)")
    grafico.set_ylabel("c (cm/Nw)")
    
    arrayx = list(x)
    arrayx.insert(0, 0)
    arrayy = list(y)
    arrayy.insert(0, y[0])

    grafico.fit(arrayx, arrayy)
    grafico.plot(x, y, "xyerrorbars", size=100, errx=xerr, erry=yerr)
    #grafico.set_grid(True)
    grafico.save(f"./Pesi/results/esperimento{esperimento}/grafico2")

grafico1(2)
grafico2(1)
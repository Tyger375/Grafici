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

def grafico3(esperimento):
    global data, grafico
    with open("./Pesi/code/data.json") as f:
        data = json.loads(f.read())

    data = data["esperimento" + str(esperimento)]
    y = data["forza"]
    x = data["peso"]
    xerr = data["El"]
    yerr = data["Ep"]

    if esperimento == 1:
        grafico = Grafico(size=(Vector2D(0, 0), Vector2D(140, 1.5)), title="l0 = 7cm", debug=True)#, xticks=1, yticks=5)
        grafico.set_x_interval(array=np.arange(0, 141, 20))
        grafico.set_y_interval(array=np.arange(0, 1.6, 0.2))
    else:
        grafico = Grafico(size=(Vector2D(0, 0), Vector2D(140, 1.5)), title="l0 = 9cm", debug=True)#, xticks=1, yticks=5)
        grafico.set_x_interval(array=np.arange(0, 141, 20))
        grafico.set_y_interval(array=np.arange(0, 1.6, 0.2))

    grafico.set_grid(True)
    grafico.set_xlabel("m (g)")
    grafico.set_ylabel("F (Nw)")
    
    arrayx = list(x)
    arrayx.insert(0, 0)
    arrayy = list(y)
    arrayy.insert(0, 0)

    grafico.fit(arrayx, arrayy)
    grafico.plot(x, y, "xyerrorbars", size=100, errx=xerr, erry=yerr)
    #grafico.set_grid(True)
    grafico.save(f"./Pesi/results/esperimento{esperimento}/grafico3")

def grafico4(esperimento):
    global data, grafico
    with open("./Pesi/code/data.json") as f:
        data = json.loads(f.read())

    data = data["esperimento" + str(esperimento)]
    y = data["g"]
    x = data["forza"]
    xerr = data["Ef"]
    yerr = data["Eg"]

    newxerr = []

    for dato in xerr:
        newxerr.append(dato/10)

    xerr = newxerr

    if esperimento == 1:
        grafico = Grafico(size=(Vector2D(0, 0.005), Vector2D(1.2, 0.015)), title="l0 = 7cm", debug=True)#, xticks=1, yticks=5)
        grafico.set_x_interval(array=np.arange(0, 1.3, 0.2))
        grafico.set_y_interval(array=np.arange(0.005, 0.016, 0.001))
    else:
        grafico = Grafico(size=(Vector2D(0, 0.005), Vector2D(1.2, 0.015)), title="l0 = 9cm", debug=True)#, xticks=1, yticks=5)
        grafico.set_x_interval(array=np.arange(0, 1.3, 0.2))
        grafico.set_y_interval(array=np.arange(0.005, 0.016, 0.001))

    grafico.set_grid(True)
    grafico.set_xlabel("F (Nw)")
    grafico.set_ylabel("g (Nw/g)")
    
    arrayx = list(x)
    #arrayx.insert(0, 0)
    arrayy = list(y)
    #arrayy.insert(0, 0)

    grafico.fit(arrayx, arrayy)
    grafico.plot(x, y, "xyerrorbars", size=100, errx=xerr, erry=yerr)
    #grafico.set_grid(True)
    grafico.save(f"./Pesi/results/esperimento{esperimento}/grafico4")    

#grafico1(2)
#grafico2(1)
grafico3(1)
#grafico4(1)
import matplotlib.pyplot as plot
import numpy as np
import json

global dati
with open("./DensitaOggetti.json") as file:
    dati = json.loads(file.read())

fig, ax = plot.subplots()
ax.set_xlabel("d (g/cm3)")
ax.set_ylabel("Oggetto/Materiale")
ax.errorbar(dati["d"], dati["oggetti"], xerr=dati["ed"], fmt="o", capsize=5)
ax.set_xticks(np.arange(0, 12, 1))
ax.grid(linestyle="--", color="gray")
plot.show()
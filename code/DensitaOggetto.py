import matplotlib.pyplot as plot
import numpy as np

dati = {
    "oggetti":[
        "CG1",
        "CG2",
        "CG3",
        "CG4",
        "P1",
        "P2",
        "P3",
        "CP1",
        "CP2",
        "CP3",
        "B"
    ],
    "m":[
        51.4,
        62.8,
        21.3,
        9.5,
        52.5,
        16.6,
        48.3,
        6.4,
        7.6,
        8.3,
        6.0
    ],
    "V":[
        8,
        8,
        8,
        8,
        6,
        6,
        6,
        1,
        1,
        1,
        2.350
    ],
    "d":[
        6.4,
        7.8,
        2.7,
        1.2,
        8.7,
        2.8,
        8.0,
        6.4,
        7.6,
        8.3,
        2.5
    ],
    "em":[
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1
    ],
    "ev":[
        0.015,
        0.015,
        0.015,
        0.015,
        0.015,
        0.015,
        0.015,
        0.015,
        0.015,
        0.015,
        0.015
    ],
    "ed":[
        0.74,
        0.90,
        0.31,
        0.14,
        1.00,
        0.32,
        0.92,
        0.74,
        0.87,
        0.95,
        0.29
    ]
}

fig, ax = plot.subplots()
ax.set_xlabel("d (g/cm3)")
ax.set_ylabel("Oggetto/Materiale")
ax.errorbar(dati["d"], dati["oggetti"], xerr=dati["ed"], fmt="o", capsize=5)
ax.set_xticks(np.arange(0, 12, 1))
ax.grid(linestyle="--", color="gray")
plot.show()

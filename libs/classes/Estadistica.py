#!/usr/bin/env python
#
import numpy as np
import pandas as pd
from plotnine import *


class Estadistica:
    def __init__(self, *args, **kwargs):
        datos, = args
        intervalos = 6 if kwargs.get('intervalos') is None else kwargs.get('intervalos')
        self.datos = datos
        self.intervalos = intervalos

    def valores(self):
        error = 0.001
        minimo = np.min(self.datos["valores"]) - error
        maximo = np.max(self.datos["valores"])
        delta = round((maximo - minimo) / self.intervalos, 3)
        particiones = np.arange(minimo, maximo + delta, delta)
        return particiones

    def frecuencias(self):
        bins = self.valores()
        self.datos["intervalos"] = pd.cut(self.datos["valores"], bins=bins)
        frecuencias = (self.datos
                       .groupby("intervalos", observed=True)
                       .agg(frecuencia=("valores", "count"))
                       .reset_index())
        print(frecuencias)
        g = (ggplot(frecuencias) +
             geom_bar(aes("intervalos", "frecuencia", fill="intervalos"), stat="identity")
             )
        g.show()
        return frecuencias

    def media(self):
        frecuencias = self.frecuencias()
        frecuencias = frecuencias["frecuencia"].values
        particiones = self.valores()
        listado1 = particiones[:-1]
        listado2 = np.delete(particiones, 0)
        valores_x = 0.5 * (listado1 + listado2)
        frecuencias_array = np.array(frecuencias)
        frecuencias_relativa = frecuencias_array / frecuencias_array.sum()
        media = (valores_x * frecuencias_relativa).sum()
        return media


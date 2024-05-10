#!/usr/bin/env python
#
import pandas as pd
from plotnine import *


class Comparar:
    def __init__(self, *args, **kwargs):
        datos, = args
        intervalos = 6 if kwargs.get('intervalos') is None else kwargs.get('intervalos')
        self.datos = datos
        self.intervalos = intervalos

    def graficar(self):
        df = pd.DataFrame(self.datos, columns=['datos'])
        g = (ggplot(df) +
             aes("datos") +
             geom_histogram(bins=self.intervalos, fill="blue") +
             labs(x="intervalos",
                  y="frecuencia",
                  title="Histograma con valores estimados")
             )
        g.show()

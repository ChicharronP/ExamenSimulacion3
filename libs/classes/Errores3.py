#!/usr/bin/env python
from enum import Enum


class Errores3(Enum):
    INTERVALO = "El intervalo no puede construirse"
    PARAMETROT = "El valor del parametro t,  no puede ser negativo"
    CANTIDAD = "No es posible generar una cantidad negativa de aleatorios"
    DECIMALES = "No es posible rredondear a una cantidad negativa"

#!/usr/bin/env python
from enum import Enum


class Errores2(Enum):
    PARAMETROA = "El parametro a no puede ser negativoo"
    PARAMETROB = "El parametro a no puede ser negativo"
    MODULO = "El modulo no puede ser negativo"
    SEMILLA = "El semilla (Xo) no puede ser negativa"
    CANTIDAD = "El numero de aleatorios por generar, no puede ser negativo"
    DECIMALES = "El numero de decimales por emplear, no puede ser negativo"
    MODULO2 = "El modulo debe ser mayor a los valores a, b y semilla"

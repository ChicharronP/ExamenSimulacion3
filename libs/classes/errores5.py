#!/usr/bin/env python
from enum import Enum


class Errores4(Enum):
    ESCALA = "La escala no puede construirse"
    CANTIDAD = "No es posible generar una cantidad negativa de alumnos"
    DECIMALES = "No es posible rredondear a una cantidad negativa"

#!/usr/bin/env python
#
# Calculo de probabilidad en funcion continua
# Diego Francisco Soto Flores
# Abril/15/2024
# al22760563.AT.ite.dot.edu.dot.mx
#
from tkinter import *

import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from libs.classes.Estadistica import Estadistica
from libs.classes.Comparar import Comparar


class Simulacion12:
    def __init__(self, root):
        self.root = root
        root.geometry('430x290')
        root.title('Calculo probabilidad v2')
        # Se crea al menu
        my_menu = Menu(root, bg='light blue', fg='black', tearoff=0)
        file_menu = Menu(my_menu, tearoff=0)
        action_menu = Menu(my_menu, tearoff=0)
        exit_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(menu=file_menu, label='Archivos')
        my_menu.add_cascade(menu=action_menu, label='Acciones')
        my_menu.add_cascade(menu=exit_menu, label='Salir')
        file_menu.add_command(label='Obtener archivo',
                              command=lambda: self.abrir_archivo())
        action_menu.add_command(label='Calculo de Media',
                                command=lambda: self.validar_promedio())
        action_menu.add_command(label='Simular',
                                command=lambda: self.validar())
        exit_menu.add_command(label='Salir',
                              command=root.quit)
        root.config(menu=my_menu)
        # Inicializan las variables
        self.data = None  # Aqui se almacena la informacion del archivo
        self.repeticiones = tk.IntVar()  # Numero de repeticiones
        self.repeticiones.set(100)
        self.media = tk.DoubleVar()  # Valor del promedio
        self.calculo = tk.StringVar()  # Indicar el tipo de calculo de probabilidad
        self.valor_inferior = tk.DoubleVar()  # Valor por calcular
        self.valor_superior = tk.DoubleVar()  # Si se declara intervalo, seria el valor superior
        self.probabilidad = tk.StringVar()  # Solucion
        # Frame para declarar los datos de entrada
        datos = Frame(root, bg='light blue')
        datos.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        datos.columnconfigure(0, weight=2)
        datos.rowconfigure(0, weight=4)
        ttk.Label(datos,
                  text="Numero de repeticiones: ",
                  justify=LEFT,
                  background='light blue').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        repeticiones = ttk.Entry(datos, textvariable=self.repeticiones)
        repeticiones.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Label(datos,
                  text="Calculo a realizar:",
                  justify=LEFT,
                  background="light blue").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        opcion = ttk.Combobox(datos,
                              textvariable=self.calculo,
                              state='readonly',
                              values=('<=', '>', 'a<=x<=b'), )
        opcion.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        opcion.current()
        ttk.Label(datos,
                  text="Limite inferior:",
                  justify=LEFT,
                  background="light blue").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(datos,
                  text="Limite superior:",
                  justify=LEFT,
                  background="light blue").grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        valor_minimo = ttk.Entry(datos, textvariable=self.valor_inferior)
        valor_minimo.grid(row=3, column=0, padx=10, pady=5)
        valor_maximo = ttk.Entry(datos, textvariable=self.valor_superior)
        valor_maximo.grid(row=3, column=1, padx=10, pady=5)
        botones = Frame(root, bg='light gray')
        botones.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        botones.columnconfigure(1, weight=3)
        botones.rowconfigure(1, weight=1)
        ttk.Button(botones,
                   text="Calcular media",
                   command=lambda: self.validar_promedio()).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Button(botones,
                   text="Simular",
                   command=lambda: self.validar()).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Button(botones,
                   text="Salir",
                   command=root.quit).grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        # Frame para mostrar los resultados
        soluciones = Frame(root, bg='light green')
        soluciones.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        soluciones.columnconfigure(2, weight=2)
        soluciones.rowconfigure(2, weight=2)
        ttk.Label(soluciones,
                  text="Media",
                  justify=LEFT,
                  background='light green').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        media = ttk.Entry(soluciones, textvariable=self.media)
        media.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Label(soluciones,
                  text="Probabilidad",
                  justify=LEFT,
                  background='light green').grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        probabilidad = ttk.Entry(soluciones, textvariable=self.probabilidad)
        probabilidad.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    @staticmethod
    def lectura(combo):
        switch = {
            '<=': 1,
            '>': 2,
            'a<=x<=b': 3
        }
        return switch.get(combo, 'e')

    def validar_promedio(self):
        bandera = 0
        if self.data is None:
            messagebox.showinfo("Falta de informacion",
                                "Seleccione archivo -> obtener archivo")
        else:
            bandera = 1
        if bandera == 1:
            estadistica = Estadistica(self.data)
            media = estadistica.media()
            self.media.set(media)

    def simular(self):
        media = self.media.get()
        repeticiones = self.repeticiones.get()
        valores_aleatorios = np.random.gumbel(3, 2, repeticiones)
        opcion = self.lectura(self.calculo.get())
        if opcion == 1:
            frecuencia = np.count_nonzero(valores_aleatorios <= self.valor_inferior.get())
        elif opcion == 2:
            frecuencia = np.count_nonzero(valores_aleatorios >= self.valor_inferior.get())
        else:
            frecuencia = (
                (self.valor_inferior.get() <= valores_aleatorios) &
                (valores_aleatorios <= self.valor_superior.get())
            ).sum()
        probabilidad = str(round((frecuencia / self.repeticiones.get()) * 100, 2)) + '%'
        self.probabilidad.set(probabilidad)
        graficar_aleatorios = Comparar(valores_aleatorios)
        graficar_aleatorios.graficar()

    def validar(self):
        bandera = 0
        if self.data is None:
            messagebox.showinfo("Error", "Se debe seleccionar una opcion el recuadro")
        else:
            bandera += 1
        if not self.calculo.get():
            messagebox.showerror("Error", "Se debe seleccionar una opcion del recuadro")
        else:
            opcion = self.lectura(self.calculo.get())
            if opcion == 3:
                if not self.valor_superior.get():
                    messagebox.showerror("Error", "Deve de indicar el límite superior del intervalo")
                else:
                    if not self.valor_inferior.get() < self.valor_superior.get():
                        messagebox.showerror("Error", "El intervalo no existe")
                    else:
                        bandera += 1
            else:
                bandera += 1
        if not self.valor_inferior.get():
            messagebox.showerror("Error", "Deve de indicar el valor de probabilidad a calcular")
        else:
            bandera += 1
        if not self.media.get():
            messagebox.showerror("Error", "Debe indicar el valor del promedio")
        else:
            bandera += 1
        if bandera >= 3:
            self.simular()

    def abrir_archivo(self):
        datos = []
        filetypes = [('Archivos CSV', '*.csv')]
        archivo = filedialog.askopenfile(filetypes=filetypes)
        if archivo is not None:
            datos = pd.read_csv(archivo)
        else:
            pass
        self.data = datos


def main():
    root = Tk()
    Simulacion12(root)
    root.mainloop()


if __name__ == '__main__':
    main()

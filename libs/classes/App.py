#!/usr/bin/env python


import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, *args):
        super().__init__()
        titulo, size, = args
        self.title(titulo)  # Titulo de la APP
        self.geometry(size)  # Pixeles
         # Estilo para los botones
        estilo = ttk.Style()
        estilo.theme_use("vista")
        """estilo.configure("TButton",
                         background="#C1E1C1",
                         foreground="black",
                         width=16,
                         borderwidth=1,
                         focusthickness=3,
                         focuscolor='none')
        estilo.map('TButton', background=[('active', 'red')])"""
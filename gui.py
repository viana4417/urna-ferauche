import tkinter as tk
from tkinter import ttk, messagebox
from eleicao import *
import pickle

class UrnaEletronicaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Urna Eletrônica")

        self.urna = None
        self.candidatos = []
        self.eleitores = []

        self.titulo_label = tk.Label(master, text="Título do Eleitor:")
        self.titulo_label.grid(row=0, column=0, padx=10, pady=10)
        self.titulo_entry = tk.Entry(master)
        self.titulo_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.buscar_eleitor_button = tk.Button(master, text="Buscar Eleitor", command=self.buscar_eleitor)
        self.buscar_eleitor_button.grid(row=0, column=2, padx=10, pady=10)

        self.eleitor_info = tk.Label(master, text="Dados do Eleitor: ", anchor="w", justify="left")
        self.eleitor_info.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")
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

        self.candidato_label = tk.Label(master, text="Número do Candidato:")
        self.candidato_label.grid(row=2, column=0, padx=10, pady=10)
        self.candidato_entry = tk.Entry(master)
        self.candidato_entry.grid(row=2, column=1, padx=10, pady=10)

        self.votar_button = tk.Button(master, text="Votar", command=self.votar)
        self.votar_button.grid(row=2, column=2, padx=10, pady=10)

        self.voto_branco_button = tk.Button(master, text="Voto Branco", command=self.voto_branco)
        self.voto_branco_button.grid(row=3, column=0, padx=10, pady=10)

        self.voto_nulo_button = tk.Button(master, text="Voto Nulo", command=self.voto_nulo)
        self.voto_nulo_button.grid(row=3, column=1, padx=10, pady=10)

        self.carregar_button = tk.Button(master, text="Carregar Dados", command=self.carregar_dados)
        self.carregar_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.listar_eleitores_button = tk.Button(master, text="Listar Eleitores", command=self.listar_eleitores)
        self.listar_eleitores_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

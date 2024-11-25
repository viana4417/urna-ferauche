import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle
from eleicao import Eleitor, Urna

class UrnaEletronicaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Urna Eletrônica Online")
        self.master.configure(background='#1e3743')
        self.master.geometry("780x430")
        self.master.resizable(True, True)
        self.master.minsize(width=400, height=300)

        self.urna = None
        self.candidatos = []
        self.eleitores = []
        self.eleitor_atual = None

        self.carregar_dados()
        self.create_interface()

    def carregar_dados(self):
        try:
            with open("candidatos.pkl", "rb") as cand_file:
                self.candidatos = pickle.load(cand_file)
            with open("eleitores.pkl", "rb") as ele_file:
                self.eleitores = pickle.load(ele_file)

            mesario = Eleitor("Mesário", "00000000", "000000000-0", 99999999, 252, 54)
            self.urna = Urna(mesario, 252, 54, self.candidatos, self.eleitores)
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivos de candidatos ou eleitores não encontrados.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
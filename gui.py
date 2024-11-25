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

    def create_interface(self):
        self.urna_frame = Frame(self.master, bd=4, bg='#D3D3D3', highlightbackground='#759fe6', highlightthickness=3)
        self.urna_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.urna_info = Frame(self.urna_frame, bd=4, bg='#808080')
        self.urna_info.place(relx=0.02, rely=0.05, relwidth=0.5, relheight=0.9)

        self.urna_teclado = Frame(self.urna_frame, bd=4, bg='#1C1C1C')
        self.urna_teclado.place(relx=0.55, rely=0.05, relwidth=0.43, relheight=0.9)

        self.display = Entry(self.urna_info, font=("Helvetica", 18), justify="center", bg="black", fg="white", insertbackground="white")
        self.display.pack(pady=10)

        self.info_label = Label(self.urna_info, text="Digite o título do eleitor", font=("Helvetica", 12), bg="#808080", fg="white")
        self.info_label.pack(pady=10)

        self.candidatos_label = Label(self.urna_info, text="", font=("Helvetica", 12), bg="#808080", fg="white", wraplength=200, justify="center")
        self.candidatos_label.pack(pady=10)

        self.create_teclado_numerico()
        self.create_buttons_acao()


    def create_teclado_numerico(self):
        botoes = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('0', 3, 1),
        ]
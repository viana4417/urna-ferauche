import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pickle
from eleicao import Eleitor, Urna

#Gabriel Viana
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

#Ricardo Nucci
    def create_teclado_numerico(self):
        botoes = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('0', 3, 1),
        ]

        for texto, linha, coluna in botoes:
            Button(self.urna_teclado, text=texto, font=("Arial", 10, "bold"), bg="#000000", fg="#FFFFFF",
                command=lambda t=texto: self.add_to_display(t)).place(
                relx=0.05 + coluna * 0.3, rely=0.1 + linha * 0.15, relwidth=0.25, relheight=0.1
            )

    def listar_eleitores(self):
        if not self.eleitores:
            messagebox.showerror("Erro", "Nenhum dado carregado.")
            return

        eleitores_str = "Eleitores Disponíveis:\n"
        for eleitor in self.eleitores:
            eleitores_str += f"Título: {eleitor.get_titulo()} - Nome: {eleitor.get_nome()}\n"

        messagebox.showinfo("Eleitores", eleitores_str)
#Daniel Perfetti
    def buscar_eleitor(self):
        if self.urna is None:
            messagebox.showerror("Erro", "Os dados da urna ainda não foram carregados.")
            return

        titulo = self.display.get()
        if not titulo.isdigit():
            messagebox.showerror("Erro", "Título do eleitor deve ser um número.")
            return

        eleitor = self.urna.get_eleitor(int(titulo))
        if eleitor:
            if eleitor.ja_votou:
                messagebox.showerror("Erro", "Este eleitor já votou.")
                self.eleitor_atual = None
                self.info_label.config(text="Nenhum eleitor selecionado.")
            else:
                self.eleitor_atual = eleitor
                self.update_side_window(eleitor)
        else:
            self.eleitor_atual = None
            messagebox.showerror("Erro", "Eleitor não encontrado.")
        self.display.delete(0, END)

#Rafael do Nascimento Maia
    def create_buttons_acao(self):
        Button(self.urna_teclado, text='BRANCO', font=("Arial", 12, "bold"), bg='white', fg='black',
            command=lambda: self.registrar_voto_especial('BRANCO')).place(relx=0.02, rely=0.7, relwidth=0.29, relheight=0.1)
        
        Button(self.urna_teclado, text='CORRIGE', font=("Arial", 12, "bold"), bg='#FF4500', fg='white',
            command=self.corrige).place(relx=0.34, rely=0.7, relwidth=0.29, relheight=0.1)
        
        Button(self.urna_teclado, text='CONFIRMA', font=("Arial", 12, "bold"), bg='#3CB371', fg='white',
            command=self.confirmar_voto).place(relx=0.66, rely=0.7, relwidth=0.33, relheight=0.1)

        Button(self.urna_teclado, text='LISTAR ELEITORES', font=("Arial", 10, "bold"), bg='#1E90FF', fg='white',
            command=self.listar_eleitores).place(relx=0.02, rely=0.82, relwidth=0.96, relheight=0.08)

        Button(self.urna_teclado, text='SELECIONAR ELEITOR', font=("Arial", 10, "bold"), bg='#32CD32', fg='white',
            command=self.buscar_eleitor).place(relx=0.02, rely=0.91, relwidth=0.96, relheight=0.08)

#Caique Tavares
    def add_to_display(self, value):
        self.display.insert(END, value)

    def corrige(self):
        self.display.delete(0, END)

    def voto_branco(self):
        self.registrar_voto_especial(0)

    def confirmar_voto(self):
        if not self.eleitor_atual:
            messagebox.showerror("Erro", "Nenhum eleitor foi selecionado.")
            return

        try:
            numero_candidato = int(self.display.get())
            self.urna.registrar_voto(self.eleitor_atual, numero_candidato)

            self.salvar_votos()

            messagebox.showinfo("Sucesso", "Voto registrado com sucesso!")

            self.eleitor_atual = None
            self.info_label.config(text="Nenhum eleitor selecionado.")
            self.candidatos_label.config(text="")

            self.display.delete(0, END)
        except ValueError:
            messagebox.showerror("Erro", "Número inválido!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
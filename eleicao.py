import pickle
from typing import List
from common import *
from datetime import date
from Interface_Eleicao import *
import csv

class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {}

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor: Eleitor, n_cand: int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        elif n_cand == 0:
            self.__votos["BRANCO"] += 1
        else:
            self.__votos["NULO"] += 1

        self.salvar_votos_txt()


    def __str__(self):
        data_atual = date.today()
        info = (f'Urna da seção {self.__secao}, zona {self.__zona}\n'
                f'Mesario {self.mesario}\n')
        info += f'{data_atual.ctime()}\n'

        for k, v in self.__votos.items():
            info += f'Candidato {k} = {v} votos\n'

        return info

    def to_csv(self):
        with open(f'urna_{self.__secao}_{self.__zona}.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Título do Eleitor Presente'])
            for eleitores in self.__eleitores:
                writer.writerow([self.__secao, self.__zona, eleitores.get_titulo()])

    def to_txt(self):
        with open(f'urna_{self.__secao}_{self.__zona}.txt', mode='w') as file:
                file.write(self.__str__())

                for eleitor in self.__eleitores:
                    file.write(f'{eleitor.get_titulo()}\n')

    def salvar_votos_txt(self):
        with open("votos.txt", "w") as arquivo_txt:
            arquivo_txt.write("Resultado da Votação:\n")
            for candidato, votos in self.__votos.items():
                arquivo_txt.write(f"{candidato}: {votos} votos\n")



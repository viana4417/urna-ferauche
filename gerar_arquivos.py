import pickle
from eleicao import Candidato, Eleitor

def gerar_arquivos():
    candidatos = [
        Candidato("Ze do Coco", "12312312", "213213-1", 43),
        Candidato("Maria da Feira", "2345545", "213213-2", 34)
    ]

    eleitores = [
        Eleitor("Jose da Silva", "3132132", "21321130-1", 11232131, 252, 54),
        Eleitor("Maria da Silva", "356777232", "132121130-X", 112321212, 252, 54),
        Eleitor("Atanásio Schneider", "31243243", "3424235-X", 11232114, 252, 54)
    ]

    with open("candidatos.pkl", "wb") as cand_file:
        pickle.dump(candidatos, cand_file)

    with open("eleitores.pkl", "wb") as ele_file:
        pickle.dump(eleitores, ele_file)

    print("Arquivos gerados com sucesso!")

if __name__ == "__main__":
    gerar_arquivos()

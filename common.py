from abc import ABC, abstractmethod
import hashlib

class Pessoa(ABC):
    __nome : str
    __RG : str
    __CPF : str

    def __init__(self, nome, RG, CPF):
        self.__nome = nome
        self.__RG = RG
        self.__CPF = CPF

    def __str__(self):
        info = (f'Nome: {self.__nome}\n'
               f'RG: {self.__RG}\n'
               f'CPF: {self.__CPF}\n')
        return info

    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', RG='{self.__RG}', CPF='{self.__CPF}')"

    def get_nome(self):
        return self.__nome

    @abstractmethod
    def assinatura_eletronica(self):
        pass

class Eleitor:
    def __init__(self, nome, RG, cpf, titulo, secao, zona):
        self.nome = nome
        self.titulo = titulo
        self.cpf = cpf
        self.zona = zona
        self.secao = secao
        self.ja_votou = False

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Título: {self.titulo}\n"
                f"Seção: {self.secao}\n"
                f"Zona: {self.zona}\n")

    def __repr__(self):
        return (f"Eleitor(nome='{self.nome}', titulo='{self.titulo}', cpf='{self.cpf}', "
                f"zona={self.zona}, secao={self.secao}, ja_votou={self.ja_votou})")

    def get_titulo(self):
        return self.titulo

    def get_nome(self):
        return self.nome

    def assinatura_eletronica(self):
        dados_para_hash = self.__str__()
        dados_em_byte = dados_para_hash.encode('utf-8')
        hash = hashlib.sha256(dados_em_byte)
        return hash.hexdigest()

class Candidato(Pessoa):
    __numero : int

    def __init__(self, nome, RG, CPF, numero):
        super().__init__(nome, RG, CPF)
        self.__numero = numero

    def __str__(self):
        info = super().__str__()
        info += (f'Numero: {self.__numero}\n')
        return info

    def __repr__(self):
        return f"Candidato({super().__repr__()}, numero='{self.__numero})'"

    def get_numero(self):
        return self.__numero

    def assinatura_eletronica(self):
        dados_para_hash = self.__str__()
        dados_em_byte = dados_para_hash.encode('utf-8')
        hash = hashlib.md5(dados_em_byte)
        return hash.hexdigest()

class Juiz(Pessoa):
    __registro : int

    def __init__(self, nome : str, RG : str , CPF : str, registro :int):
        super().__init__(nome, RG, CPF)
        self.__registro = registro

    def __str__(self):
        info = super().__str__()
        info += f'Registro: {self.__registro}'
        return info

    def assinatura_eletronica(self):
        dados_para_hash = self.__str__()
        dados_em_byte = dados_para_hash.encode('utf-8')
        hash = hashlib.sha1(dados_em_byte)
        return hash.hexdigest()
class Personagem:
    def __init__(self, nome, idade, energia=0, dinheiro=0, ansiedade=0):
        self.__nome = nome
        self.__idade = idade
        self.__energia = energia
        self.__dinheiro = dinheiro
        self.__ansiedade = ansiedade
        self.__fase = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        self.__energia += valor

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, valor):
        self.__dinheiro += valor

    @property
    def ansiedade(self):
        return self.__ansiedade

    @ansiedade.setter
    def ansiedade(self, valor):
        self.__ansiedade -= valor

    def passar_fase(self):
        self.__fase += 1

    def decisao(self, energia, dinheiro, ansiedade):
        self.__energia -= energia
        self.__dinheiro -= dinheiro
        self.__ansiedade += ansiedade
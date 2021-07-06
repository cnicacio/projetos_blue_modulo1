from character import Personagem

class Geracaoz(Personagem):
    def __init__(self, nome, idade, energia, dinheiro, ansiedade):
        super().__init__(nome, idade, energia, dinheiro, ansiedade)


    def __str__(self):
        return f'''
        ESTAGIÁRIO GERAÇÃO Z:

        Personagem: {self.nome}
        Idade: {self.idade}
        Energia: {self.energia}
        Dinheiro: {self.dinheiro}
        Ansiedade: {self.ansiedade}
        '''
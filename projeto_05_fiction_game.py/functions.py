from character import Personagem
from boomer import Boomer
from gen_z import Geracaoz

def cafedamanha(self, escolha):
    if escolha == 1:
        self.__energia -= 5
        self.__ansiedade -= 5
    else:
        self.__energia += 5
        self.__ansiedade += 10
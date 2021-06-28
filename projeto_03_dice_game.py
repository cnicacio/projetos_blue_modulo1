'''
PROJETO 03- JOGO DE DADOS

Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
O programa tem que:
• Perguntar quantas rodadas você quer fazer;
• Guardar os resultados dos dados em um dicionário.
• Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
• Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.
'''

from random import randint # sorteará os números que cada jogador tirará no dado por rodada
from random import sample # sorteia a ordem que cada jogador jogará o dado na rodada
from time import sleep # tempo entre as jogadas
from operator import itemgetter # importa a biblioteca itemgetter para ordenar o dicionário do maior para o menor valor

dice = dict() # dicionário com as jogadas dos jogos de dados
players = list() # armazena os nomes dos jogadores em uma lista
points = [0, 0, 0, 0] # armazena os pontos dos jogadores em uma lista

# lista com os resultados possíveis do jogo de dados de 6 lados
results = ['''
+-------+
|       |
|   @   |
|       |
+-------+
''',
'''
+-------+
| @     |
|       |
|     @ |
+-------+
''',
'''
+-------+
| @     |
|   @   |
|     @ |
+-------+
''',
'''
+-------+
| @   @ |
|       |
| @   @ |
+-------+
''',
'''
+-------+
| @   @ |
|   @   |
| @   @ |
+-------+
''',
'''
+-------+
| @   @ |
| @   @ |
| @   @ |
+-------+
''']

for i in range(4): # cria os quatro jogadores para o jogo e salva-os na lista 'players'
    player = str(input(f'Digite o nome do jogador {i+1}: ')).strip().title()
    players.append(player)

while True: # condição verdadeira = o usuário está jogando
    
    round = int(input('Informe o número de rodadas desejadas: ')) # recebe o número de jogadas

    for r in range(round): # para cada jogada determinada em 'round', armazenará as informações no dicionário 'dice'
        
        for p in sample(range(4), 4): # criará uma jogada para cada jogador em ordem aleatória ("sorteia" os jogadores que iniciarão a rodada)
            dice[f'{players[p]}'] = randint(1,6) # no dicionário, cada jogador terá gerado seu número do dado (de 1 a 6)

        # imprimirá uma sequência de resultados para cada rodada determinada em 'round'
        print(f'\n\nRODADA {r+1}:\n') 

        for k, v in dice.items(): # para cada chave 'k' e valor 'v' no dicionário 'dice', retorna o número que cada jogador tirou no dado
            print(f'''O jogador {k} jogou:
            {results[v-1]}
            ''')
            sleep(2)

        sorted_dice = dict(sorted(dice.items(), key=itemgetter(1),reverse=True)) # retornará o dicionário ordenado pelos valores, do maior para o menor

        sorted_values = list(sorted_dice.values()) # lista somente com as chaves para determinação do vencedor da rodada
        sorted_keys = list(sorted_dice.keys()) # lista somente com os valores para determinação do vencedor da rodada

        if sorted_values[0] == sorted_values[1]: # se o maior valor tirado for repetido, a rodada termina empatada
            print(f'A rodada foi empatada!\n')
        else: # se não houver repetição no maior valor, declara um vencedor
            print(f'{sorted_keys[0]} venceu a rodada!\n')
            winner = players.index(sorted_keys[0]) # retorna o índice do vencedor na lidta 'players'
            points[winner] += 1 # soma 1 ponto ao índice do vencedor na lista 'points'

    maximum = max(points) # retornará o maior valor da lista de pontos, ou seja, o vencedor
    champion = players[points.index(maximum)] # retornará o jogador que foi campeão a partir do mesmo índice da lista 'points' que possui o valor máximo
    sorted_points = sorted(points) # ordena a lista do maior para o menor número de pontos

    if sorted_points[0] == sorted_points[1]: # se houver dois ou mais valores de máximo iguais na lista de pontos, o jogo termina empatado
        print(f'O jogo de dados com {round} rodadas terminou empatado!\n')
    else: # caso contrário, há um vencedor
        print(f'O grande campeão é {champion} com {maximum} vitorias\n')

    # pergunta ao usuário se quer continuar jogando, só sai do loop se o usuário não quiser continuar ('N')
    new_game = str(input('Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    while new_game not in 'SN': # repete a pergunta até que seja inserida uma opção válida
        new_game = str(input('Opção inválida! Deseja jogar novamente [S/N]? ')).strip().upper()[0]

    if new_game == 'N': # sai do loop
        break

print('OBRIGADO POR JOGAR! ATÉ A PRÓXIMA')
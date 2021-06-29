from random import randint # sorteará os números que cada jogador tirará no dado por rodada
from random import sample # sorteia a ordem que cada jogador jogará o dado na rodada
from time import sleep # tempo entre as jogadas
from operator import itemgetter # importa a biblioteca itemgetter para ordenar o dicionário do maior para o menor valor
import os # limpar o console no início do jogo e caso o usuário queira jogar novamente

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

os.system('cls||clear') # limpa o console no início do código

for i in range(4): # cria os quatro jogadores para o jogo e salva-os na lista 'players'
    player = str(input(f'Digite o nome do jogador {i+1}: ')).strip().title()
    players.append(player)

while True: # condição verdadeira = o usuário está jogando
    round = int(input('Informe o número de rodadas desejadas: ')) # recebe o número de jogadas

    for r in range(round): # para cada jogada determinada em 'round', armazenará as informações no dicionário 'dice'
        for p in sample(range(4), 4): # criará uma jogada para cada jogador em ordem aleatória ("sorteia" os jogadores que iniciarão a rodada)
            dice[f'{players[p]}'] = randint(1,6) # no dicionário, cada jogador terá gerado seu número do dado (de 1 a 6)
        
        print(f'\n\nRODADA {r+1}:\n') # imprimirá uma sequência de resultados para cada rodada determinada em 'round'

        for k, v in dice.items(): # para cada chave 'k' e valor 'v' no dicionário 'dice', retorna o número que cada jogador tirou no dado
            print(f'''O jogador {k} jogou:
            {results[v-1]}
            ''')
            sleep(2) # 2 segundos de intervalo entre as jogadas de cada um

        sorted_dice = dict(sorted(dice.items(), key=itemgetter(1),reverse=True)) # retornará o dicionário ordenado pelos valores, do maior para o menor
        sorted_values = list(sorted_dice.values()) # lista somente com as chaves para determinação do vencedor da rodada
        sorted_keys = list(sorted_dice.keys()) # lista somente com os valores para determinação do vencedor da rodada

        if sorted_values[0] == sorted_values[1]: # se o maior valor tirado for repetido, a rodada termina empatada
            print(f'A rodada foi empatada!\n')
        else: # se não houver repetição no maior valor, declara um vencedor
            print(f'{sorted_keys[0]} venceu a rodada!\n')
            winner = players.index(sorted_keys[0]) # retorna o índice do vencedor na lista 'players'
            points[winner] += 1 # soma 1 ponto ao índice do vencedor na lista 'points'

    maximum = max(points) # retornará o maior valor da lista de pontos, ou seja, o vencedor
    champion = players[points.index(maximum)] # retornará o jogador que foi campeão a partir do mesmo índice da lista 'points' que possui o valor máximo
    sorted_points = sorted(points,reverse=True) # ordena a lista do maior para o menor número de pontos
    result = dict(zip(players,points)) # cria um dicionário com os jogadores e o número de vitórias de cada um

    for a, b in result.items(): # retornará o número de vitórias de cada jogador
        print(f'{a}: {b} vitória(s)')
    if sorted_points[0] == sorted_points[1]: # se houver dois ou mais valores de máximo iguais na lista de pontos, o jogo termina empatado
        print(f'O jogo de dados com {round} rodadas terminou empatado!\n')
    else: # caso contrário, há um vencedor
        print(f'O grande campeão é {champion} com {maximum} vitoria(s)\n')
    
    new_game = str(input('Deseja jogar novamente [S/N]? ')).strip().upper()[0] # pergunta ao usuário se quer continuar jogando, só sai do loop se o usuário não quiser continuar ('N')
    while new_game not in 'SN': # repete a pergunta até que seja inserida uma opção válida
        new_game = str(input('Opção inválida! Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    if new_game == 'N': # sai do loop / fim de jogo
        break
    else:
        os.system('cls||clear') # limpa o console e reinicia o loop, perguntando novamente o número de jogadas

print('OBRIGADO POR JOGAR! ATÉ A PRÓXIMA') # fim de jogo
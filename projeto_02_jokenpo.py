'''
Projeto 02 – Jogo Jokenpô
Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você. O programa tem que:
• Permitir que eu decida quantas rodadas iremos fazer;
• Ler a minha escolha (Pedra, papel ou tesoura);
• Decidir de forma aleatória a decisão do computador;
• Mostrar quantas rodadas cada jogador ganhou;
• Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
• Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.
'''

from random import randint
from time import sleep

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

jogador = computador = empate = 0 # variáveis para definir o número de vitórias do usuário/computador ou empates

while True:
    jogadas = int(input('Digite o número de jogadas: '))
    for c in range(jogadas): # para o número de jogadas definidas, repete-se o que segue
        jogada = int(input('FAÇA A SUA JOGADA\nPedra [1]\nPapel [2]\nTesoura [3]\n'))

        while jogada < 1 or jogada > 3: # tratamento de erro para o jogador inserir a jogada corretamente
            jogada = int(input('Digite corretamente. Pedra [1], papel [2] ou tesoura? [3] '))
        comp_jogada = randint(1,3) # computador "sorteará" um número entre 1 e 3 para fazer a sua jogada aleatória

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')

        if comp_jogada == 1: # COMPUTADOR JOGOU PEDRA
            print(f'O computador jogou:\n{pedra}')
        if comp_jogada == 2: # COMPUTADOR JOGOU PAPEL
                print(f'O computador jogou:\n{papel}')
        if comp_jogada == 3: # COMPUTADOR JOGOU TESOURA
                print(f'O computador jogou:\n{tesoura}')

        if jogada == 1: # USUÁRIO JOGOU PEDRA
            print(f'Você jogou:\n{pedra}')
        elif jogada == 2: # USUÁRIO JOGOU PAPEL
            print(f'Você jogou:\n{papel}')
        elif jogada == 3: # USUÁRIO JOGOU TESOURA
            print(f'Você jogou:\n{tesoura}')

        if (jogada - comp_jogada) == 0: # EMPATE (NÚMEROS IGUAIS NA RODADA)
            print('RODADA EMPATADA!')
            empate += 1 # contabiliza empate
        elif (jogada - comp_jogada) == 1 or (jogada - comp_jogada) == -2: # COMBINAÇÃO DE RESULTADOS PARA A VITÓRIA DO USUÁRIO
            print('VOCÊ VENCEU!')
            jogador += 1 # contabiliza vitória do usuário
        elif (jogada - comp_jogada) == -1 or (jogada - comp_jogada) == 2: # COMBINAÇÃO DE RESULTADOS PARA A VITÓRIA DO COMPUTADOR
            print('VOCÊ PERDEU!')
            computador += 1 # contabiliza vitória do computador

    novamente = str(input('Deseja jogar novamente [S/N]? ')).strip().upper()[0] # ao fim do range(jogadas), ou seja, após o número de rodadas definida pelo usuário, pergunta-se se o jogador quer jogar novamente
    while novamente not in 'SN': # tratamento de erro para o jogador inserir a opção corretamente
        novamente = str(input('Resposta inválida! Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    if novamente == 'N': # se a resposta for não, sai do loop e vai para as verificações de vencedor
        break

print(f'''Você venceu {jogador} rodadas 
O computador venceu {computador} rodadas
Houveram {empate} rodadas empatadas''') # contagem dos vencedores das rodadas

if jogador > computador: # o vencedor é o jogador
    print(f'Você é o grande vencedor!')

elif jogador < computador: # o vencedor é o computador
    print(f'O computador é o grande vencedor!')

else: # em caso de empate
    print(f'O grande duelo foi empatado!')

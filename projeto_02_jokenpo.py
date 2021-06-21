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

jogador = 0
computador = 0

while True:
    jogadas = int(input('Digite o número de jogadas: '))
    for c in range(jogadas):
        jogada = str(input(''' FAÇA A SUA JOGADA
        Pedra [1] 
        Papel [2] 
        Tesoura [3]      
        '''))

        if jogada not in '123':
            jogada = str(input('Digite corretamente. Pedra [1], papel [2] ou tesoura? [3] '))
        comp_jogada = str(randint(1,3))

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')

        if comp_jogada == '1': # COMPUTADOR JOGOU PEDRA
            print(f'O computador jogou:\n{pedra}')
            if jogada == '1':
                print(f'Você jogou:\n{pedra}\n\nEMPATE!')
            if jogada == '2':
                print(f'Você jogou:\n{papel}\n\nVOCÊ VENCEU!')
                jogador += 1
            if jogada == '3':
                print(f'Você jogou:\n{tesoura}\n\nVOCÊ PERDEU!')
                computador += 1

        if comp_jogada == '2': # COMPUTADOR JOGOU PAPEL
            print(f'O computador jogou:\n{papel}')
            if jogada == '1':
                print(f'Você jogou:\n{pedra}\n\nVOCÊ PERDEU!')
                computador += 1
            if jogada == '2':
                print(f'Você jogou:\n{papel}\n\nEMPATE!')
            if jogada == '3':
                print(f'Você jogou:\n{tesoura}\n\nVOCÊ VENCEU!')
                jogador += 1

        if comp_jogada == '3': # COMPUTADOR JOGOU TESOURA
            print(f'O computador jogou:\n{tesoura}')
            if jogada == '1':
                print(f'Você jogou:\n{pedra}\n\nVOCÊ VENCEU!')
                jogador += 1
            if jogada == '2':
                print(f'Você jogou:\n{papel}\n\nVOCÊ PERDEU!')
                computador += 1
            if jogada == '3':
                print(f'Você jogou:\n{tesoura}\n\nEMPATE!')
    
    novamente = str(input('Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    while novamente not in 'SN':
        novamente = str(input('Resposta inválida! Deseja jogar novamente [S/N]? ')).strip().upper()[0]
    if novamente == 'N':
        break

print(f'''Você venceu {jogador} rodadas
O computador venceu {computador} rodadas
''')
if jogador > computador:
    print('Você é o grande vencedor!')
elif jogador < computador:
    print('O computador é o grande vencedor!')
else:
    print('O grande duelo foi empatado!')
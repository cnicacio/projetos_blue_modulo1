from datetime import datetime
from time import sleep
import os

os.system('cls||clear')

print('''
ELEIÇÕES 2021:

Tabela de candidatos:

====================
  N°     Candidato
====================
  1     Candidato 1
  2     Candidato 2
  3     Candidato 3
  4        Nulo
  5       Branco
====================
''')

candidates = ['Candidato 1', 'Candidato 2', 'Candidato 3', 'Nulo', 'Branco']
votes = [0,0,0,0,0]

def voting():
    while True:
        candidate = int(input('Digite o número do seu candidato: '))
        while candidate < 1 or candidate > 5:
            candidate = int(input('Opção inválida! Digite o número do seu candidato: '))

        confirm = str(input('Deseja confirmar o seu voto [S/N]? ')).strip().upper()[0]
        while confirm not in 'SN':
            confirm = str(input('Opção inválida! Deseja confirmar o seu voto [S/N]? ')).strip().upper()[0]
        if confirm == 'S':
            votes[candidate - 1] += 1
            break

def authorization(person, age):
    if age < 16:
        vote_type = 'NEGADO'
        print(f'{person}, seu voto é {vote_type}!')
    elif 18 <= age <= 70:
        vote_type = 'OBRIGATÓRIO'
        print(f'{person}, seu voto é {vote_type}!')
        return voting()
    else:
        vote_type = 'OPCIONAL'
        print(f'{person}, seu voto é {vote_type}!')
        optional = str(input('Você deseja votar [S/N]? ')).strip().upper()[0]
        while optional not in 'SN':
            optional = str(input('Opção inválida! Você deseja votar [S/N]? ')).strip().upper()[0]
        if optional == 'S':
            return voting()
        else:
            return 'Obrigado pela resposta!'

def general_results():
    results_dict = dict(zip(candidates,votes))
    for k, v in results_dict.items():
        print(f'{k}: {v} voto(s) - {100*(v/sum(votes)):.2f} %')

def valid_results():
    valid_candidates = candidates[0:3]
    valid_votes = votes[0:3]
    valid_results_dict = dict(zip(valid_candidates,valid_votes))

    for a, b in valid_results_dict.items():
        print(f'{a}: {100*(b/sum(valid_votes)):.2f} % dos votos válidos')
    
    max_votes = max(valid_votes)
    winner = valid_candidates[valid_votes.index(max_votes)]
    
    if sorted(valid_votes)[-1] > sorted(valid_votes)[-2]:
        print(f'\nO vencedor das eleições é {winner}')
    else:
        print(f'\nHouve um empate técnico nestas eleições')


while True:
    elector = str(input('Digite seu nome completo: ')).strip().title()
    birth_year = int(input('Digite seu ano de nascimento: '))
    elector_age = datetime.now().year - birth_year
    authorization(elector, elector_age)
    more_electors = str(input('Deseja continuar cadastrando eleitores [S/N]? ')).strip().upper()[0]
    while more_electors not in 'SN':
        more_electors = str(input('Deseja continuar cadastrando eleitores [S/N]? ')).strip().upper()[0]
    if more_electors == 'N':
        break

os.system('cls||clear')

print('APURAÇÃO DE VOTOS EM ANDAMENTO...')
sleep(2)
for i in range(1,101, +1):
    print (f'{i} % dos votos apurados')
    sleep(0.001)

print('APURAÇÃO FINALIZADA!!')
sleep(2)

os.system('cls||clear')

print('RESULTADO GERAL DAS ELEIÇÕES:')
general_results()
sleep(2)
print('RESULTADO POR VOTOS VÁLIDOS DAS ELEIÇÕES:')
valid_results()
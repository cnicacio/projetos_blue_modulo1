from datetime import datetime # será utilizada no cálculo da idade do eleitor
from time import sleep # será utilizada para mostrar os resultados ao final do programa
import os # será utilizada para limpar o console ao final de cada voto

os.system('cls||clear') # limpa o console para rodar o programa

# tabela com a lista dos candidatos e opções de branco e nulo
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

candidates = ['Candidato 1', 'Candidato 2', 'Candidato 3', 'Nulo', 'Branco'] # lista com os candidatos, definirá os votos gerais
votes = [0,0,0,0,0] # lista com o número de votos gerais, para os candidatos, incluindo votos brancos e nulos

def voting(): # função voting, para realizar a votação de cada eleitor cadastrado
    while True: # a condição verdadeira é a pessoa estar votando
        candidate = int(input('Digite o número do seu candidato: '))
        while candidate < 1 or candidate > 5: # tratamento de erros para que o eleitor não vote em nenhum número que não possa votar
            candidate = int(input('Opção inválida! Digite o número do seu candidato: '))

        confirm = str(input('Deseja confirmar o seu voto [S/N]? ')).strip().upper()[0] # confirma o voto no candidato escolhido. Caso contrário, volta a perguntar o número do candidato para o eleitor
        while confirm not in 'SN': # tratamento de erros para que o eleitor confirme de fato o seu voto ou não
            confirm = str(input('Opção inválida! Deseja confirmar o seu voto [S/N]? ')).strip().upper()[0]
        if confirm == 'S': # caso o voto seja confirmado, encerra a função saindo do loop
            votes[candidate - 1] += 1
            break

def authorization(person, age): # função para autorizar o voto de cada eleitor cadastrado no programa
    if age < 16: # se a idade for menor que 16 anos, o voto é negado e a função voting() não é chamada
        vote_type = 'NEGADO'
        print(f'{person}, seu voto é {vote_type}!')
    elif 18 <= age <= 70: # chama obrigatoriamente a função voting() pois o eleitor terá de votar
        vote_type = 'OBRIGATÓRIO'
        print(f'{person}, seu voto é {vote_type}!')
        return voting() # executa a função voting() dentro da função authorization()
    else: # chama a função voting() somente se o eleitor optar por votar, respondendo com 'S' o input requisitado na variável optional
        vote_type = 'OPCIONAL'
        print(f'{person}, seu voto é {vote_type}!')
        optional = str(input('Você deseja votar [S/N]? ')).strip().upper()[0]
        while optional not in 'SN': # tratamento de erro para que o eleitor faça a opção entre votar ou não votar corretamente
            optional = str(input('Opção inválida! Você deseja votar [S/N]? ')).strip().upper()[0]
        if optional == 'S':
            return voting() # executa a função voting() dentro da função authorization()
        else:
            return 'Obrigado pela resposta!'

def general_results(): # função utilizada para apurar os votos totais, incluindo brancos e nulos
    results_dict = dict(zip(candidates,votes)) # dicionário utilizado para apresentar os votos de cada candidato, incluindo brancos e nulos, bem como a porcentagem correspondente a cada um deles sob os votos gerais (chaves = candidatos, valores = número de votos)
    
    if sum(votes) != 0: # tratamento de erro para apresentar os resultados somente se houver comparecimento de eleitores na eleição
        for k, v in results_dict.items(): # para cada candidato, imprime no console os votos recebidos e a porcentagem geral
            print(f'{k}: {v} voto(s) - {100*(v/sum(votes)):.2f} %\n')
    else: # mensagem para convocação de novas eleições caso não haja eleitores
        print('Nenhum eleitor compareceu às eleições! Um novo pleito deverá ser convocado!')

def valid_results(): # função utilizada para apurar os votos válidos, ou seja, somente os votos em candidatos, excluindo brancos e nulos da apuração
    if sum(votes) != 0: # tratamento de erro para apresentar os resultados somente se houver comparecimento de eleitores na eleição
        valid_candidates = candidates[0:3] # fatiamento da lista candidates para apresentar somente os candidatos da eleição, excluindo brancos e nulos
        valid_votes = votes[0:3] # fatiamento da lista votes para apresentar somente os votos em candidatos da eleição, excluindo brancos e nulos
        valid_results_dict = dict(zip(valid_candidates,valid_votes)) # dicionário utilizado para apresentar os votos de cada candidato, excluindo brancos e nulos, bem como a porcentagem correspondente a cada um deles sob os votos gerais (chaves = candidatos, valores = número de votos)

        for a, b in valid_results_dict.items(): # para cada candidato, imprime no console os votos recebidos e a porcentagem geral
            if sum(valid_votes) != 0: # tratamento de erro para apresentar os resultados somente se houver comparecimento de eleitores na eleição
                print(f'{a}: {100*(b/sum(valid_votes)):.2f} % dos votos válidos\n')

        max_votes = max(valid_votes) # guarda o maior número de votos na lista valid_votes em uma variável
        winner = valid_candidates[valid_votes.index(max_votes)] # busca o nome do candidato mais votado a partir do índice do maior número de votos

        if sorted(valid_votes)[-1] > sorted(valid_votes)[-2]: # verificação de empate nas eleições
            print(f'\nO vencedor das eleições é {winner}') # caso não haja empate, retorna o vencedor
        else: # caso haja empate, retorna mensagem sobre o segundo turno das eleições
            print(f'\nHouve um empate técnico nestas eleições! Haverá segundo turno para desempate!')
            
    else: # mensagem para convocação de novas eleições caso não haja eleitores
        print('Nenhum eleitor compareceu às eleições! Um novo pleito deverá ser convocado!')


while True: # condição verdadeira é um eleitor estar sendo cadastrado e votando
    elector = str(input('Digite seu nome completo: ')).strip().title() # pergunta o nome do eleitor, para verificação de idade na chegada à urna de votação
    birth_year = int(input('Digite seu ano de nascimento: ')) # pergunta o ano de nascimento do eleitor, para verificar se o voto será autorizado
    elector_age = datetime.now().year - birth_year # calcula a idade do eleitor
    authorization(elector, elector_age) # com o nome e a idade, retorna a função authorization() com os parâmetros nome e idade, autorizando ou não o voto e executando a sequência para que o eleitor registre seu voto, caso o voto seja obrigatório ou o eleitor com voto opcional deseje votar
    os.system('cls||clear') # limpa o console por segurança, para ocultar os dados dos eleitores cujos votos já foram cadastrados, garantindo o voto secreto
    
    more_electors = str(input('Deseja continuar cadastrando eleitores [S/N]? ')).strip().upper()[0] # pergunta ao mesário se haverão mais eleitores no pleito
    while more_electors not in 'SN': # tratamento de erro para forçar o mesário a responder 'S' ou 'N'
        more_electors = str(input('Deseja continuar cadastrando eleitores [S/N]? ')).strip().upper()[0]
    if more_electors == 'N': # sai do loop somente se o mesário não for cadastrar mais eleitores
        break

os.system('cls||clear') # limpa o console por segurança, para ocultar os dados dos eleitores cujos votos já foram cadastrados, garantindo o voto secreto

print('APURAÇÃO DE VOTOS EM ANDAMENTO...')
sleep(2)
for i in range(1,101, +1): # contagem de apuração de votos
    print (f'{i} % dos votos apurados')
    os.system('cls||clear')
    sleep(0.005)

print('APURAÇÃO FINALIZADA!!')
sleep(2)

os.system('cls||clear')

print('\nRESULTADO GERAL DAS ELEIÇÕES:\n')
general_results() # retorna o resultado das eleições com votos gerais
sleep(2)
print('\nRESULTADO POR VOTOS VÁLIDOS DAS ELEIÇÕES:\n')
valid_results() # retorna o resultado das eleições com votos válidos

from quadrantes import jogo
from funcionalidades import verificador_de_vitoria, simbolo, executar_jogada

from time import sleep
from random import random
from random import choice
from copy import deepcopy
import os

RESTAURADOR = deepcopy(jogo)

def mostrar_jogo(jogo):

    for i in jogo:
        print(''.join(i))


def jogada(tabela_quadrantes, jogo, cpu=False):

    if cpu:  # cpu joga
        return choice(tabela_quadrantes)

    else:
        while True:
            try:
                opcao = int(input('Escolha um quadrante para jogar\n>> '))
            except (TypeError, ValueError):
                os.system('cls')
                mostrar_jogo(jogo)

                print('Por favor, escolha corretamente.')
            else:
                if opcao not in tabela_quadrantes:
                    os.system('cls')
                    mostrar_jogo(jogo)

                    print('Por favor, escolha corretamente.')
                else:
                    return opcao
                

def exec_tabela_jogo(jogo, jogador, quadrante):
    if jogador[0] == '\\':
        jogador = 1  # xis
    else:
        jogador = 2  # bolinha

    if quadrante in [1, 2, 3]:
        jogo[0][quadrante - 1] = jogador

    elif quadrante in [4, 5, 6]:
        jogo[1][quadrante - 4] = jogador
    else:
        jogo[2][quadrante - 7] = jogador


os.system('cls')

while True:
    nome = input('Digite seu nome: ')
    jogo = deepcopy(RESTAURADOR)

    os.system('cls')
    print(f'\nSEJA BEM VINDO, {nome.title()}')

    while True:
        try:
            opcao = int(input('\nEscolha seu símbolo: \n\n   ( )\n1. ( )\n\n   \\ /\n2. / \\ \n\n>> '))
            
        except (TypeError, ValueError):
            os.system('cls')
            print('Por favor, escolha corretamente.')
        else:
            if opcao in [1, 2]:
                break
            else:
                os.system('cls')
                print('Por favor, escolha corretamente.')
    
    if opcao == 1:
        jogador = simbolo('bolinha')
        cpu = simbolo('xis')
    else:
        jogador = simbolo('xis')
        cpu = simbolo('bolinha')
    
    os.system('cls')
    print('Tenha um bom jogo...')
    sleep(1)
    os.system('cls')

    TABELA_QUADRANTES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    INTERCALADOR = True  # o usuário começa jogando
    _JOGO = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0] 
    ]

    while True:
        if INTERCALADOR:  # usuario jogando
            mostrar_jogo(jogo)
            opcao = jogada(TABELA_QUADRANTES, jogo)

            executar_jogada(opcao, jogador, jogo)
            TABELA_QUADRANTES.remove(opcao)
            INTERCALADOR = False

            exec_tabela_jogo(_JOGO, jogador, opcao)

        else:
            opcao = jogada(TABELA_QUADRANTES, jogo, cpu=True)

            executar_jogada(opcao, cpu, jogo)
            TABELA_QUADRANTES.remove(opcao)
            INTERCALADOR = True

            exec_tabela_jogo(_JOGO, cpu, opcao)
        
        os.system('cls')
        
        if INTERCALADOR:  # a cpu está jogando
            alguem_venceu = verificador_de_vitoria(_JOGO, cpu)

            if alguem_venceu:
                mensagem = 'VOCÊ PERDEU, TENTE NOVAMENTE :('

                i = 84

                for caracter in mensagem:
                    jogo[14][i] = caracter
                    i += 1

                mostrar_jogo(jogo)
                break
        
        elif INTERCALADOR == False:
            alguem_venceu = verificador_de_vitoria(_JOGO, jogador)

            if alguem_venceu:
                mensagem = 'PARABÉNS, VOCÊ GANHOU :)'

                i = 84

                for caracter in mensagem:
                    jogo[14][i] = caracter
                    i += 1

                mostrar_jogo(jogo)
                break
        
        if len(TABELA_QUADRANTES) == 0:
            mensagem = 'DEU VELHA, TENTE NOVAMENTE :('

            i = 84

            for caracter in mensagem:
                jogo[14][i] = caracter
                i += 1

            mostrar_jogo(jogo)
            break
            
    
    continuar = input('Deseja jogar novamente? [S/N] ').upper()
    while continuar[0] not in ['S', 'N']:
        continuar = input('Por favor, responda apenas [S/N] ').upper()
    
    if continuar[0] == 'N':
        break
    else:
        os.system('cls')        


os.system('cls')
print('OBRIGADO POR JOGAR, VOLTE SEMPRE :))')

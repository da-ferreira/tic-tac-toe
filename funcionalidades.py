
from quadrantes import jogo, quadrantes
import os

def simbolo(symbol):
    # o usuário escolheu bolinha
    if symbol == 'bolinha':  
        bolinha = ['(', ' ', ')',
               '(', ' ', ')'
            ]

        return bolinha

    # o usuário escolheu xis
    else:  
        xis = [
            '\\', ' ', '/',
            '/', ' ', '\\'
        ]

        return xis


def executar_jogada(quadrant, jogador, jogo):
    i = 0
    
    for j in quadrantes[quadrant]:
        jogo[j[0]][j[1]] = jogador[i]
        i += 1


def verificador_de_vitoria(jogo, simbolo_jogador):
    if simbolo_jogador[0] == '\\':
        simbolo_jogador = 1  # o usuário escolheu xis
    else:
        simbolo_jogador = 2  # o usuário escolheu bolinha


    for linha in jogo:
        if all(x == simbolo_jogador for x in linha):
            return True  # caso alguém tenha ganhado
    
    for i in range(3):
        temp = []

        for j in range(3):
            temp.append(jogo[j][i])
        
        if all(x == simbolo_jogador for x in temp):
            return True
    
    temp = [
        [jogo[0][0], jogo[1][1], jogo[2][2]],  # primeira diagonal
        [jogo[0][2], jogo[1][1], jogo[2][0]]  # segunda diagonal
    ]


    if all(x == simbolo_jogador for x in temp[0]) or all(x == simbolo_jogador for x in temp[1]):
        return True

    return False  # caso ninguém tenha vencido ainda


if __name__ == "__main__":
    jog = simbolo('xis')

    a = [
        [2, 1, 1],
        [0, 1, 0],
        [1, 0, 2] 
    ]


    '''while True:
        for i in jogo:
            print(''.join(i))

        x = int(input('Local: '))

        jogada(x, jog)

        os.system('cls')'''
    
    print(verificador_de_vitoria(a, jog))
    
        
    
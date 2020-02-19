#AULA 18 - JOGO DE ADIVINHAÇÃO EM PYTHON

import random

erros = 0
sorteado = random.randrange(0,100)
jogador = int(input("Digite seu número: "))

while (sorteado != jogador):
    if (sorteado > jogador):
        print("ERRO, o número é maior!")
    elif (sorteado < jogador):
        print("ERRO, o número é menor!")
    erros += 1
    jogador = int(input("Digite seu número: "))

print("\nNúmero:", jogador, "- você acertou em", (erros + 1), 'tentativas')
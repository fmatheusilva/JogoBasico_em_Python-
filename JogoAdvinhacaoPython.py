#Jogo de Advinhação

import random
import os

erro=0
sorteado=random.randrange(0,100)

jogador=int(input("Digite seu número: "))
while(sorteado != jogador):
    os.system("cls")
    if(sorteado < jogador):
        print("Errou, o número é menor :c")
    if(sorteado > jogador):
        print("Errou, o número é maior :c")
    erro = erro + 1
    jogador = int(input("Digite seu número: "))

print("Numero " + str(jogador) + ", você acertou em " + str(erro+1) + " tentativas");
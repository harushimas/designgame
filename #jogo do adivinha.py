#jogo do adivinha
from random import randint 
print("seja bem vindo!")
print("digite um número de 1 a 100")
sorteado = randint(1, 100)
chute = 0 
while chute != sorteado:
    chute = int(input("chute:"))
    if chute == sorteado:
        print("você ganhou!")
    else:
        if chute > sorteado:
            print("alto")
        else:
            print("baixo")
print("fim de jogo!")
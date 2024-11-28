#repetição 2.0
def repete_nome(nome,vezes):
    nome = input("escreva seu nome:")
    vezes = int(input("desja repetir quantas vezes?"))
    x = 1
    while x<=vezes:
        print(nome)
        #x=x+1 
        x+=1 
nome = input("digite o nome:")
vezes = int(input("quantas vezes deseja repetir?"))
repete_nome(nome,vezes)
print("término")
print("")
print("---------")
repete_nome(nome,vezes)
print("cabou,cabou")
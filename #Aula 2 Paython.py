#Aula 2 Paython
#Aula 10/10/24
#Variável de memoria
nome   = 'Maria'
idade1 = 16
valor  = 23
valor1 = 20
valor2 = 2

resultado=valor1+valor2

print('Bom dia')
print(resultado)
#---------------------------------------------
Nome      = 'Carlos'
idade2    = 19
valor3    = 20.5
exame_med = True
#---------------------------------------------
print('O valor da veriavel idade vezes 2 é',idade2*2)
print(type(nome))
print(type(idade1))
print(type(valor3))
print(type(exame_med))
#---------------------------------------------
jogador  = 'Pedro'
nivel    = 3
credito  = 10
vida     = 90

if vida>=0:
    print('Continua o jogo')
else:
    print('Se fudeu')
#---------------------------------------------
if nivel==1:
    print('codigos do nivel 1')
elif nivel==2:
    print('codigos do nivel 2')
elif nivel==3:
    print("codigos do nivel 3")
elif nivel==4:
    print('codigos do nivel 4')
elif nivel==5:
    print('codigos do nivel 5')
else: 
    print("nivel indisponivel")
#---------------------------------------------
print("-----Cadastro Aluno-----")
print('-----Digite os Dados-----')
nome2=input("Digite nome Jogador: ")
Nivel_Atual=input("Digite o nivel: ")

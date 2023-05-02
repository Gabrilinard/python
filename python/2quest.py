import random 
jogador11 = int(input('Qual é seu primeiro chute?'))
jogador12 = int(input('Qual é seu segundo chute?'))
jogador13 = int(input('Qual é seu terceiro chute?'))
jogador21 = int(input('Qual é seu primeiro chute?'))
jogador22 = int(input('Qual é seu segundo chute?'))
jogador23 = int(input('Qual é seu terceiro chute?'))
jogador31 = int(input('Qual é seu primeiro chute?'))
jogador32 = int(input('Qual é seu segundo chute?'))
jogador33 = int(input('Qual é seu terceiro chute?'))
maquina1 = random.randint (1,1)
maquina2 = random.randint (1,1)
maquina3 = random.randint (1,1)
valor1 = 150000
resultado = 0
print('Máquina 1 colocou:{}'.format(maquina1))
print('Máquina 2 colocou:{}'.format(maquina2))
print('Máquina 3 colocou:{}'.format(maquina3))

if (jogador11 == maquina1 or jogador11 == maquina2 or jogador11 == maquina3) and (jogador12 == maquina1 or jogador12 == maquina2 or jogador12 == maquina3) and (jogador13 == maquina1 or jogador13 == maquina2 or jogador13 == maquina3):
    print('Parabéns!')
    resultadof = resultado + 1  

if (jogador21 == maquina1 or jogador21 == maquina2 or jogador21 == maquina3) and (jogador22 == maquina1 or jogador22 == maquina2 or jogador22 == maquina3) and (jogador23 == maquina1 or jogador23 == maquina2 or jogador13 == maquina3):
    print('Parabéns!')
    resultadof = resultado +1

if (jogador31 == maquina1 or jogador31 == maquina2 or jogador31 == maquina3) and (jogador32 == maquina1 or jogador22 == maquina2 or jogador32 == maquina3) and (jogador33 == maquina1 or jogador33 == maquina2 or jogador13 == maquina3):
    print('Parabéns!')
    resultadof = resultado +1

if resultadof == 1 or resultadof == 2 or resultadof == 3:
    valor = valor1/resultadof
    print('O valor final ficou: {}'.format(valor))
elif resultadof == 0:
    print('Ninguém ganhou.')


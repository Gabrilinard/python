import random 
usuario = int(input('Digite um número entre 1 e 10 para a disputa:'))
while (usuario > 10 or usuario < 1): 
    print('Número Inválido! Digite um número entre 1 e 10.')
    usuario = int(input('Digite um número entre 1 e 10 para a disputa:'))

maquina = random.randint (1,10)
print('Máquina colocou: {}'.format(maquina))

if usuario == maquina:
    print('Parabéns')
else: 
    print('Você não ganhou o sorteio.')

while usuario != maquina:
    usuario = int(input('Digite um número entre 1 e 10 para a disputa novamente:'))
    print('Máquina colocou: {}'.format(maquina))
import random 

parouimpar = int(input('Escolha: [1]- impar ou [2] - par?'))
eu = int(input('Digite um número de 0 a 10:'))
while(eu > 10) or (eu < 0):
    print('[ERROR] Digite um número válido!') 
    parouimpar = int(input('Escolha: [1]- impar ou [2] - par?'))
    eu = int(input('Digite um número de 0 a 10:'))
maquina = random.randint(0,10)
soma = eu + maquina 
print('A máquina colocou: {}'.format(maquina))

if(parouimpar == 2 and soma % 2 == 0) or (parouimpar == 1 and soma % 2 != 0):
    print('Parabéns, você ganhou!!')
else: 
    print('Máquina ganhou!') 
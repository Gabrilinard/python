import random  
lista = ['pedra','papel','tesoura']
pepate = (input("Digite pedra, papel ou tesoura:"))
maquina = random.choice(lista)
print('Máquina colocou {}'.format(maquina))

while (pepate =='tesoura' and maquina =='tesoura') or (pepate =='papel' and maquina =='papel' ) or (pepate =='pedra' and maquina =='pedra'):
    print('Empate! Tente novamente!')
    pepate = (input("Digite pedra, papel ou tesoura:"))
    maquina = random.choice(lista)
    print('Máquina colocou {}'.format(maquina))

if(pepate =='pedra' and maquina =='tesoura') or (pepate =='papel' and maquina =='pedra') or (pepate =='tesoura' and maquina =='papel'): 
    print('Parabéns, você ganhou!')
else: 
    print('Máquina ganhou!') 

 
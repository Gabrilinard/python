saldo = 0
digite = 0
while (digite != 4):
    digite = int(input('Digite 1 - Consultar o saldo \n 2 - Sacar \n 3 - Depositar \n 4 - Sair ' ))
    if digite == 1: 
        print('O saldo é igual a: {}'.format(saldo))
    elif digite == 2:
        sacar = int(input('Qual o valor do saque?'))
        print('O valor do saque foi: {}'.format(sacar))
        saldo -= sacar
        print('Agora você tem {}'.format(saldo) , 'de saldo.')
    elif digite == 3:
        depositar = int(input('Qual o valor que você deseja depositar?'))
        print('Você depositou: {}'.format(depositar))
        saldo += depositar
        print('Agora você tem {}'.format(saldo) , 'de saldo.')
    elif digite == 4:
        print('Você saiu!')
        break

        
    
time1 = str(input('Digite o primeiro time da partida:'))
time2 = str(input('Digite o segundo time da partida:'))
qntdegolstime1 = int(input('Quantos gols o primeiro time fez?'))
qntdegolstime2 = int(input('Quantos gols o segundo time fez?'))

if qntdegolstime1 > qntdegolstime2:
    print('{} venceu!!'.format(time1))
elif qntdegolstime1 < qntdegolstime2: 
    print('{} venceu!!'.format(time2))
elif qntdegolstime1 == qntdegolstime2: 
    print('EMPATE.')
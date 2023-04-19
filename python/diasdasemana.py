diadasemana = int(input('Digite um número de 1 a 7:'))
while diadasemana > 7 or diadasemana < 1:
    print('Número inválido! Digite um número entre 1 e 7.')
    diadasemana = int(input('Digite um número de 1 a 7:'))

if diadasemana == 1:
    print('Hoje é segunda.')
elif diadasemana == 2:
    print('Hoje é terça.')
elif diadasemana == 3:
    print('Hoje é quarta.')
elif diadasemana == 4:
    print('Hoje é quinta.')
elif diadasemana == 5:
    print('Hoje é sexta.')
elif diadasemana == 6:
    print('Hoje é sábado.')
elif diadasemana == 7:
    print('Hoje é domingo.')
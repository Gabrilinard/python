homemoumulher = int(input('Digite 1-homem ou 2-mulher'))
qntsanos = int(input('Qual é a sua idade?'))
peso = float(input('Qual é seu peso?'))
if (homemoumulher == 1 and qntsanos > 18 and qntsanos <= 30):
    resultado1 = 7.5 * peso
    print('{}'.format(resultado1))
if (homemoumulher == 1 and qntsanos > 30 and qntsanos <= 60):
    resultado2 = 8.5 * peso
    print('{}'.format(resultado2))
if (homemoumulher == 1 and qntsanos > 60):
    resultado3 = 9.5 * peso
    print ('{}'.format(resultado3))
if (homemoumulher == 2 and qntsanos > 18 and qntsanos <=30):
    resultado4 = 4.5 * peso
    print ('{}'.format(resultado4))
if (homemoumulher == 2 and qntsanos > 30 and qntsanos <=60):
    resultado5 = 5.5 * peso
    print ('{}'.format(resultado5))
if (homemoumulher == 2 and qntsanos > 60):
    resultado6 = 6.5 * peso
    print ('{}'.format(resultado6))


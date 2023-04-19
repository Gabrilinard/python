medida1 = int(input('Digite o tamanho do primeiro lado do triângulo:'))
medida2 = int(input('Digite o tamanho do segundo lado do triângulo:'))
medida3 = int(input('Digite o tamanho do terceiro lado do triângulo:'))

if medida1 + medida2 > medida3:
    print('Ok, medidas válidas para construir um triângulo!')

while medida1 + medida2 < medida3:
    print('Infelizmente, as medidas mencionadas são inviáveis para construir um triângulo.')
    medida1 = int(input('Digite o tamanho do primeiro lado do triângulo:'))
    medida2 = int(input('Digite o tamanho do segundo lado do triângulo:'))
    medida3 = int(input('Digite o tamanho do terceiro lado do triângulo:'))

if medida1 + medida2 > medida3:
    print('Ok, medidas válidas para construir um triângulo!')

if medida1 == medida2 == medida3:
    print('O triângulo é equilátero!')
elif medida1 != medida2 != medida3:
    print('O triângulo é escaleno')
elif medida1 == medida2 != medida3 or medida1 == medida3 != medida2 or medida2 == medida3 != medida1:
    print('O triângulo é isósceles')

salario = float(input('Digite seu salário:'))
emprestimo = float(input('Digite o emprestimo:'))
meses = int(input('Digite a quantidade de meses:'))
taxa = float(input('Digite a taxa de meses:'))
prestacao = emprestimo/meses * taxa
if prestacao > salario * 30/100 + salario:
    print('Você não pode pagar.')
else: 
    print('Você pode pegar!')
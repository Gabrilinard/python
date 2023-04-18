valor_produto = float(input('Digite o valor do produto:'))
tipo_pagamento = int(input('Digite [1] - Pagamento com Crédito, [2] - Pagamento com Débito, [3] - Pagamento com Pix ou [4] - Pagamento em Espécie'))

if (tipo_pagamento == 3) or (tipo_pagamento == 4):
    print('Você irá ter um desconto de 10%. O valor ficará {}'.format(valor_produto - valor_produto * 10 / 100))
elif (tipo_pagamento == 2):
    print('Você irá ter um desconto de 5%. O valor ficará {}'.format(valor_produto - valor_produto * 5 / 100))
elif (tipo_pagamento == 1):
    quantasvzs = int(input('Em quantas vezes você quer fazer o seu pagamento?'))
    if (quantasvzs < 2 and quantasvzs > 0):
        print('O valor ficará o mesmo! Logo, você pagará {}'.format(valor_produto))
    else:
        print('O valor do produto terá um acréscimo de 20%. Então o valor ficará: {}'.format(valor_produto + valor_produto * 20 / 100))

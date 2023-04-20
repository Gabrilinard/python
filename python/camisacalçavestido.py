camisaqntp = 0
camisaqntm = 0
camisaqntg = 0
calcaqntp = 0
calcaqntm = 0
calcaqntg = 0
vestidoqntp = 0 
vestidoqntm = 0 
vestidoqntg = 0


funcao = int(input('Deseja adicionar, pesquisar ou vender algum produto? Para Adicionar-1, Pesquisar-2, Vender-3:'))
while funcao > 3 or funcao < 1:
    print('Número inválido! Digite um número entre 1 e 3.')
    funcao = int(input('Deseja adicionar, pesquisar ou vender algum produto? Para Adicionar - 1, Pesquisar - 2, Vender - 3:'))

if funcao == 1:
    produto = int(input('Qual produto você deseja adicionar? 1-Camisa, 2-Calça ou 3-Vestido:'))
    while produto > 3 or produto < 1:
        print('Número inválido! Digite um número entre 1 e 3.')
        produto = int(input('Qual produto você deseja adicionar? 1 - Camisa, 2 - Calça ou 3 - Vestido:'))
    if produto == 1:
        tamanhocami = int(input('Qual o tamanho da camisa que você deseja adicionar no sistema? 1 - Camisa Pequena, 2 - Camisa Média ou 3 - Camisa Grande:'))
        while tamanhocami > 3 or tamanhocami < 1:
            print('Número inválido! Digite um número entre 1 e 3.')
            tamanhocami = int(input('Qual o tamanho da camisa que você deseja adicionar no sistema? 1 - Camisa Pequena, 2 - Camisa Média ou 3 - Camisa Grande:'))
        if tamanhocami == 1:
            qntcamisapa = int(input('Quantas camisas pequenas você deseja adicionar?'))
            addqntcamisaestoqp = camisaqntp + qntcamisapa
            print('{} camisas pequenas no estoque.'.format(addqntcamisaestoqp))
        elif tamanhocami == 2:
            qntcamisama = int(input('Quantas camisas médias você deseja adicionar?'))
            addqntcamisaestoqm = camisaqntm + qntcamisama
            print('{} camisas médias no estoque'.format(addqntcamisaestoqm))
        elif tamanhocami == 3:
            qntcamisaga = int(input('Quantas camisas grandes você deseja adicionar?'))
            addqntcamisaestoqg = camisaqntg + qntcamisaga
            print('{} camisas grandes no estoque.'.format(addqntcamisaestoqg))
    if produto == 2:
        tamanhocalc = int(input('Qual o tamanho da calça que você deseja adicionar no sistema? 1-Calça Pequena, 2-Calça Média ou 3-Calça Grande:'))
        while tamanhocalc > 3 or tamanhocalc < 1:
            print('Número inválido! Digite um número entre 1 e 3.')
            tamanhocalc = int(input('Qual o tamanho da calça que você deseja adicionar no sistema? 1-Calça Pequena, 2-Calça Média ou 3-Calça Grande:'))
        if tamanhocalc == 1:
            qntcalcp = int(input('Quantas calças pequenas você deseja adicionar?'))
            addqntcalcaestoqp = calcaqntp + qntcalcp
            print('{} calças pequenas no estoque.'.format(addqntcalcaestoqp))
        elif tamanhocalc == 2:
            qntcalcm = int(input('Quantas calças médias você deseja adicionar?'))
            addqntcalcaestoqm = calcaqntm + qntcalcm
            print('{} calças médias no estoque'.format(addqntcamisaestoqm))
        elif tamanhocalc == 3:
            qntcalcg = int(input('Quantas calças grandes você deseja adicionar?'))
            addqntcalcaestoqg = calcaqntg + qntcalcg
            print('{} calças grandes no estoque.'.format(addqntcalcaestoqg))
    if produto == 3:
        tamanhovest = int(input('Qual o tamanho do vestido que você deseja adicionar no sistema? 1-Vestido Pequeno, 2-Vestido Médio ou 3-Vestido Grande:'))
        while tamanhovest > 3 or tamanhovest < 1:
            print('Número inválido! Digite um número entre 1 e 3.')
            tamanhovest = int(input('Qual o tamanho do vestido que você deseja adicionar no sistema? 1-Vestido Pequeno, 2-Vestido Médio ou 3-Vestido Grande:'))
        if tamanhovest == 1:
            qntvestp = int(input('Quantos vestidos pequenos você deseja adicionar?'))
            addqntvestestoqp = vestidoqntp + qntvestp
            print('{} vestidos pequenos no estoque.'.format(addqntvestestoqp))
        elif tamanhovest == 2:
            qntvestm = int(input('Quantos vestidos médios você deseja adicionar?'))
            addqntvestestoqm = vestidoqntm + qntvestm
            print('{} vestidos médios no estoque.'.format(addqntvestestoqm))
        elif tamanhovest == 3:
            qntvestg = int(input('Quantos vestidos grandes você deseja adicionar?'))
            addqntvestestoqg = vestidoqntg + qntvestg
            print('{} vestidos grandes no estoque.'.format(addqntvestestoqg))

    

if funcao == 2:
    qualproduto = int(input('Qual produto você deseja pesquisar a quantidade? 1 - Camisa, 2 - Calça ou 3 - Vestido:'))
    while qualproduto > 3 or qualproduto < 1:
        print('Número inválido! Digite um número entre 1 e 3.')
        qualproduto = int(input('Qual produto você deseja pesquisar a quantidade? 1 - Camisa, 2 - Calça ou 3 - Vestido:'))
    if qualproduto == 1:
        print('{} CAMISAS PEQUENAS'.format(addqntcamisaestoqp))
        print('{} CAMISAS MÉDIAS'.format(addqntcamisaestoqm))
        print('{} CAMISAS GRANDES'.format(addqntcamisaestoqg))
    if qualproduto == 2:
        print('{} CALÇAS PEQUENAS'.format(addqntcalcaestoqp))
        print('{} CALÇAS MÉDIAS'.format(addqntcalcaestoqm))
        print('{} CALÇAS GRANDES'.format(addqntcalcaestoqg))
    if qualproduto == 3:
        print('{} VESTIDOS PEQUENOS'.format(addqntvestestoqp))
        print('{} VESTIDOS MÉDIOS'.format(addqntvestestoqm))
        print('{} VESTIDOS GRANDES'.format(addqntvestestoqg))

if funcao == 3:
    produtovenda = int(input('Qual produto você deseja vender? 1-Camisa, 2-Calça ou 3-Vestido:'))
    while produtovenda > 3 or produtovenda < 1:
        print('Número inválido! Digite um número entre 1 e 3.')
        produtovenda = int(input('Qual produto você deseja vender? 1 - Camisa, 2 - Calça ou 3 - Vestido:'))
    if produtovenda == 1:
        vendatamanhocami = int(input('Qual o tamanho da camisa que você deseja vender? 1-PEQUENA, 2-MÉDIA OU 3-GRANDE:'))
        while vendatamanhocami > 3 or vendatamanhocami < 1:
            print('Número inválido! Digite um número entre 1 e 3.')
            vendatamanhocami = int(input('Qual o tamanho da camisa que você deseja vender? 1-PEQUENA, 2-MÉDIA OU 3-GRANDE:'))
        if vendatamanhocami == 1: 
            qntvendacamip = int(input('Quantas camisas pequenas você deseja vender?'))
            addqntcamisaestoqp = camisaqntp - qntvendacamip 
            print('Você vendeu {} camisas pequenas'.format(qntvendacamip))
            print('Restam {} camisas pequenas no estoque'.format(addqntcamisaestoqg))
        if vendatamanhocami == 2:
            qntvendacamim = int(input('Quantas camisas médias você deseja vender?'))
            addqntcamisaestoqm = camisaqntm - qntvendacamim 
            print('Você vendeu {} camisas médias'.format(qntvendacamim))
            print('Restam {} camisas médias no estoque'.format(addqntcamisaestoqm))
        if vendatamanhocami == 3:
            qntvendacamig = int(input('Quantas camisas grandes você deseja vender?'))
            addqntcamisaestoqg = camisaqntg - qntvendacamig
            print('Você vendeu {} camisas grandes'.format(qntvendacamig))
            print('Restam {} camisas grandes no estoque'.format(addqntcamisaestoqg))
    if produtovenda == 2:
        vendatamanhocalc = int(input('Qual o tamanho da calça que você deseja vender? 1 - PEQUENA, 2 - MÉDIA OU 3 - GRANDE'))
        while vendatamanhocalc > 3 or vendatamanhocalc < 1:
            print('Número inválido! Digite um número entre 1 e 3.')
            vendatamanhocalc = int(input('Qual o tamanho da calça que você deseja vender? 1 - PEQUENA, 2 - MÉDIA OU 3 - GRANDE'))
        if vendatamanhocalc == 1:
            qntvendacalcp = int(input('Quantas calças pequenas você deseja vender?'))
            addqntcalcaestoqp = calcaqntp - qntvendacalcp 
            print('Você vendeu {} calças pequenas'.format(qntvendacamip))
            print('Restam {} calças pequenas no estoque'.format(addqntcalcaestoqp))
        if vendatamanhocalc == 2:
            qntvendacalcm = int(input('Quantas calças médias você deseja vender?'))
            addqntcalcaestoqm = calcaqntm - qntvendacalcm 
            print('Você vendeu {} calças médias'.format(qntvendacamim))
            print('Restam {} calças médias no estoque'.format(addqntcalcaestoqm))
        if vendatamanhocalc == 3:
            qntvendacalcg = int(input('Quantas calças grandes você deseja vender?'))
            addqntcalcaestoqg = calcaqntg - qntvendacalcg 
            print('Você vendeu {} calças grandes'.format(qntvendacamig))
            print('Restam {} calças grandes no estoque'.format(addqntcalcaestoqg))
    if produtovenda == 3:
        vendatamanhovest = int(input('Qual o tamanho do vestido que você deseja vender? 1 - PEQUENA, 2 - MÉDIA OU 3 - GRANDE'))
        while vendatamanhovest > 3 or vendatamanhovest < 1:
            print('Número inválido! Digite um número entre 1 e 3.')
            vendatamanhovest = int(input('Qual o tamanho do vestido que você deseja vender? 1 - PEQUENA, 2 - MÉDIA OU 3 - GRANDE'))
        if vendatamanhovest == 1:
            qntvendavestp = int(input('Quantos vestidos pequenos você deseja vender?'))
            addqntvestestoqp = vestidoqntp - qntvendavestp
            print('Você vendeu {} vestidos pequenos'.format(qntvendavestp))
            print('Restam {} vestidos pequenos no estoque'.format(estoquevestp))
        if vendatamanhovest == 2:
            qntvendavestm = int(input('Quantos vestidos médios você deseja vender?'))
            addqntvestestoqm = vestidoqntm - qntvendavestm
            print('Você vendeu {} vestidos médios'.format(qntvendavestp))
            print('Restam {} vestidos médios no estoque'.format(addqntvestestoqm))
        if vendatamanhovest == 3:
            qntvendavestg = int(input('Quantos vestidos grandes você deseja vender?'))
            addqntvestestoqg = vestidoqntg - qntvendavestg
            print('Você vendeu {} vestidos grandes'.format(qntvendavestg))
            print('Restam {} vestidos grandes no estoque'.format(addqntvestestoqg))







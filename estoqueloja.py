digite = 0
camisap = 0
camisam = 0
camisag = 0
calcap = 0
calcam = 0
calcag = 0
vestidop = 0 
vestidom = 0
vestidog = 0
while digite != 4:
    digite = int(input('Digite: \n 1 - Adicionar produto \n 2 - Pesquisar produto \n 3 - Vender produto \n 4 - Sair'))
    if digite == 1:
        qualproduto = int(input('Qual produto você deseja adiconar? Digite: \n 1 - Camisap \n 2 - Camisam \n 3 - Camisag \n 4 - Calçap \n 5 - Calçam \n 6 - Calçag \n 7 - Vestidop \n 8 - Vestidom \n 9 - Vestidog'))
        if qualproduto == 1:
            qntcamisap = int(input('Quantas camisasp você deseja adicionar?'))
            camisap += qntcamisap
            print('Você adicionou: {}'.format(qntcamisap) ,'camisasp. E agora possui: {}'.format(camisap) , "camisasp.")
        elif qualproduto == 2:
            qntcamisam =int(input('Quantas camisasm você deseja adicionar?'))
            camisam += qntcamisam
            print('Você adicionou: {}'.format(qntcamisam) ,'camisasm. E agora possui: {}'.format(camisam) , "camisasm.")
        elif qualproduto == 3:
            qntcamisag =int(input('Quantas camisasg você deseja adicionar?'))
            camisag += qntcamisag
            print('Você adicionou: {}'.format(qntcamisag) ,'camisasg. E agora possui: {}'.format(camisag) , "camisasg.")
        elif qualproduto == 4:
            qntcalcap =int(input('Quantas calçasp você deseja adicionar?'))
            calcap += qntcalcap
            print('Você adicionou: {}'.format(qntcalcap) ,'calçasp. E agora possui: {}'.format(calcap) , "calçasp.")
        elif qualproduto == 5:
            qntcalcam =int(input('Quantas calçasm você deseja adicionar?'))
            calcam += qntcalcam
            print('Você adicionou: {}'.format(qntcalcam) ,'calçasm. E agora possui: {}'.format(calcam) , "calçasm.")
        elif qualproduto == 6:
            qntcalcag =int(input('Quantas calçasg você deseja adicionar?'))
            calcag += qntcalcag
            print('Você adicionou: {}'.format(qntcalcag) , 'calçasg. E agora possui: {}'.format(calcag) , "calçasg.")
        elif qualproduto == 7:
            qntvestidop =int(input('Quantos vestidosp você deseja adicionar?'))
            vestidop += qntvestidop
            print('Você adicionou: {}'.format(qntvestidop) ,'vestidosp. E agora possui: {}'.format(vestidop) , "vestidosp.")
        elif qualproduto == 8:
            qntvestidom =int(input('Quantos vestidosm você deseja adicionar?'))
            vestidom += qntvestidom
            print('Você adicionou: {}'.format(qntvestidom) ,'vestidosm. E agora possui: {}'.format(vestidom) , "vestidosm.")
        elif qualproduto == 9:
            qntvestidog =int(input('Quantos vestidosg você deseja adicionar?'))
            vestidog += qntvestidog
            print('Você adicionou: {}'.format(qntvestidog) ,'vestidosg. E agora possui: {}'.format(vestidog) , "vestidosg.")

    if digite == 2:
        pesquisar = int(input('Qual produto você deseja saber quantos tem? Digite: \n 1 - Camisap \n 2 - Camisam \n 3 - Camisag \n 4 - Calçap \n 5 - Calçam \n 6 - Calçag \n 7 - Vestidop \n 8 - Vestidom \n 9 - Vestidog'))
        if pesquisar == 1:
            print('{}'.format(camisap), 'camisasp no estoque.')
        elif pesquisar == 2:
            print('{}'.format(camisam), 'camisasm no estoque.')
        elif pesquisar == 3:
            print('{}'.format(camisag), 'camisasg no estoque.')
        elif pesquisar == 4:
            print('{}'.format(calcap), 'calçasp no estoque.')
        elif pesquisar == 5:
            print('{}'.format(calcam), 'calçasm no estoque.')
        elif pesquisar == 6:
            print('{}'.format(calcag), 'calçasg no estoque.')
        elif pesquisar == 7:
            print('{}'.format(vestidop), 'vestidosp no estoque.')
        elif pesquisar == 8:
         print('{}'.format(vestidom), 'vestidosm no estoque.')
        elif pesquisar == 9:
            print('{}'.format(vestidog), 'vestidosg no estoque.')

    if digite == 3:
        vender = int(input('Qual produto você deseja vender? Digite: \n 1 - Camisap \n 2 - Camisam \n 3 - Camisag \n 4 - Calçap \n 5 - Calçam \n 6 - Calçag \n 7 - Vestidop \n 8 - Vestidom \n 9 - Vestidog'))
        if vender == 1:
            qntcamisapv = int(input('Quantas camisasp você deseja vender?'))
            camisap -= qntcamisapv
            print('Você vendeu: {}'.format(qntcamisapv) ,'camisasp. E agora possui: {}'.format(camisap) , "camisasp.")
        elif vender == 2:
            qntcamisamv = int(input('Quantas camisasm você deseja vender?'))
            camisam -= qntcamisamv
            print('Você vendeu: {}'.format(qntcamisamv) ,'camisasm. E agora possui: {}'.format(camisam) , "camisasm.")
        elif vender == 3:
            qntcamisagv = int(input('Quantas camisasg você deseja vender?'))
            camisag -= qntcamisagv
            print('Você vendeu: {}'.format(qntcamisagv) ,'camisasg. E agora possui: {}'.format(camisag) , "camisasg.")
        elif vender == 4:
            qntcalcapv = int(input('Quantas calçasp você deseja vender?'))
            calcap -= qntcalcapv
            print('Você vendeu: {}'.format(qntcalcapv), 'calçasp. E agora possui: {}'.format(calcap), 'calçasp')
        elif vender == 5:
            qntcalcamv = int(input('Quantas calçasm você deseja vender?'))
            calcam -= qntcalcamv
            print('Você vendeu: {}'.format(qntcalcamv), 'calçasm. E agora possui: {}'.format(calcam), 'calçasm')
        elif vender == 6:
            qntcalcagv = int(input('Quantas calçasg você deseja vender?'))
            calcag -= qntcalcagv
            print('Você vendeu: {}'.format(qntcalcagv), 'calçasg. E agora possui: {}'.format(calcag), 'calçasg')
        elif vender == 7:
            qntvestidopv = int(input('Quantos vestidosp você deseja vender?'))
            vestidop -= qntvestidopv
            print('Você vendeu: {}'.format(qntvestidopv) ,'vestidosp. E agora possui: {}'.format(vestidop) , "vestidosp.")
        elif vender == 8:
            qntvestidomv = int(input('Quantos vestidosm você deseja vender?'))
            vestidom -= qntvestidomv
            print('Você vendeu: {}'.format(qntvestidomv) ,'vestidosm. E agora possui: {}'.format(vestidom) , "vestidosm.")
        elif vender == 9:
            qntvestidogv = int(input('Quantos vestidosg você deseja vender?'))
            vestidog -= qntvestidogv
            print('Você vendeu: {}'.format(qntvestidogv) ,'vestidosg. E agora possui: {}'.format(vestidog) , "vestidosg.")

    if digite == 4:
        print('Você saiu!')
        break
        
        

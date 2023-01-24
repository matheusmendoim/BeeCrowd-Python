ossos = input()
tipo = input()
alimentacao = input()

if ossos == 'vertebrado':
    if tipo == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if alimentacao == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if tipo == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if alimentacao == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
# 1- Carnes - proteinas
# 2- Cereais - carboidratos
# 3- Outros - vitaminas e minerais

from random import sample

grupo_alimento = [
    [
        {
            'alimento':'carne de boi, magra',
            'grupo':1,
            'porcao':100,
            'calorias':111,
            'proteinas':21,
            'gorduras':3,
            'carboidratos':0
        },
        {
            'alimento':'carne de porco, magra',
            'grupo':1,
            'porcao':100,
            'calorias':181,
            'proteinas':19,
            'gorduras':12,
            'carboidratos':0
        },
        {
            'alimento':'carne de galinha, magra',
            'grupo':1,
            'porcao':100,
            'calorias':149,
            'proteinas':21,
            'gorduras':7,
            'carboidratos':0
        },
        {
            'alimento':'carne de soja',
            'grupo':1,
            'porcao':50,
            'calorias':170,
            'proteinas':26,
            'gorduras':1,
            'carboidratos':15
        },
    ],
    [
        {
            'alimento':'arroz integral',
            'grupo':2,
            'porcao':100,
            'calorias':350,
            'proteinas':8,
            'gorduras':2,
            'carboidratos':75
        },
        {
            'alimento':'milho integral',
            'grupo':2,
            'porcao':100,
            'calorias':129,
            'proteinas':3,
            'gorduras':1,
            'carboidratos':28
        },
        {
            'alimento':'granola',
            'grupo':2,
            'porcao':50,
            'calorias':161,
            'proteinas':5,
            'gorduras':3,
            'carboidratos':27
        },
        {
            'alimento':'aveia em flocos',
            'grupo':2,
            'porcao':50,
            'calorias':173,
            'proteinas':7,
            'gorduras':1,
            'carboidratos':28
        },
    ],
    [
        {
            'alimento':'abacaxi',
            'grupo':3,
            'porcao':100,
            'calorias':52,
            'proteinas':0,
            'gorduras':0,
            'carboidratos':14
        },
        {
            'alimento':'açaí',
            'grupo':3,
            'porcao':100,
            'calorias':247,
            'proteinas':4,
            'gorduras':12,
            'carboidratos':37
        },
        {
            'alimento':'feijão preto',
            'grupo':3,
            'porcao':100,
            'calorias':319,
            'proteinas':24,
            'gorduras':2,
            'carboidratos':51
        },
        {
            'alimento':'batata-doce',
            'grupo':3,
            'porcao':100,
            'calorias':125,
            'proteinas':2,
            'gorduras':1,
            'carboidratos':28
        },
    ]
]

def mostrar_alimentos():
    grupo = grupo_alimento[sample(range(3),1)]
    alimento = grupo[sample(range(4),1)]
    return alimento

def mostrar_combinações(combinacoes):
    print('Numero de combinações: {}'.format(len(combinacoes)))
    for combinacao in combinacoes:
        soma = 0
        for alimento in combinacao:
            soma += alimento['calorias']
            for param,val in alimento.items():
                print('{}:{}\t'.format(param,val), end=' ')
            print('\n')
        print('------------------- TOTAL CALORIAS: {} --------------------'.format(soma))

def combinacoes(calorias):
    """
    Retorna todas combinações de alimentos sem ultrapassar o limite de calorias dado
    """
    res_combinacoes = []
    for primeiro in grupo_alimento[0]:
        soma1 = 0
        combina1 = []
        if primeiro['calorias'] < calorias:
            soma1 += primeiro['calorias']
            combina1.append(primeiro)
        else:
            continue
        for segundo in grupo_alimento[1]:
            soma2 = soma1
            combina2 = combina1.copy()
            if segundo['calorias']+soma2 < calorias:
                soma2 += segundo['calorias']
                combina2.append(segundo)
            else:
                continue
            for terceiro in grupo_alimento[2]:
                combina3 = combina2.copy()
                if terceiro['calorias']+soma2 < calorias:
                    combina3.append(terceiro)
                    res_combinacoes.append(combina3)
                else:
                    continue
    
    if not res_combinacoes:
        return False
    
    return res_combinacoes


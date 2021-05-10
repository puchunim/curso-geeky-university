def ex001(num):
    """
    Crie uma função que recebe como parâmetro
    um número inteiro e devolve o seu dobro.
    """

    return num * 2


def ex002(data):
    """
    Faça uma função que receba a data atual e exiba
    na tela no formato textual por extenso. (formato DD/MM/AAAA)
    """

    meses = {
        "01" : "janeiro",
        "02" : "fevereiro",
        "03" : "março",
        "04" : "abril",
        "05" : "maio",
        "06" : "junho",
        "07" : "julho",
        "08" : "agosto",
        "09" : "setembro",
        "10" : "outubro",
        "11" : "novembro",
        "12" : "dezembro"
    }

    dia, mes, ano = data.split('/')

    return f'{int(dia)} de {meses[mes]} de {ano}'


def ex003(num):
    """
    Faça uma função para verificar se um número é
    positivo ou negativo. Sendo que o valor de retorno
    será 1 se positivo, -1 se negativo e 0 se for 0.
    """

    if num == 0:
        return 0

    elif num > 0:
        return 1

    else:
        return -1


def ex004(num): #pulado
    """
    Faça uma função para verificar se um número é um quadrado perfeito.
    Um quadrado perfeito é um número inteiro não negativo que pode ser expresso
    como o quadrado de outro número inteiro.
    """

    pass

# FEOIWUGF(UEW(TEJIOGJKWEGKJEWJKGEW))ÇFÇLEWÇGLWE
# então....
# pois é.
# é assim que eu sou.

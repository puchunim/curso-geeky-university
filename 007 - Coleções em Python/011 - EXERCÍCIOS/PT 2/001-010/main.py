def ex001():
    """
    Leia uma matriz 4x4, conte e escreva
    quantos valores maiores que 10 ela possui.
    """

    matriz = [[], [], [], []]
    for row in range(0, 4):
        for n in range(0, 4):
            matriz[row].append(
                int(input(f'Digite o {n+1}° valor para a coluna {row+1}: '))
            )
        print('===+===')

    maisde10 = 0
    for row in matriz:
        print(row)
        for n in row:
            if n > 10:
                maisde10 += 1

    print(f'Existem {maisde10} números maiores de 10 na matriz!')

def ex002():
    """
    Declare uma matriz 5x5. Preencha com 1 a diagonal
    principal e com 0 os demais elementos. Escreva ao final
    a matriz obtida.
    """

    matriz = [[] for _ in range(0, 10)]

    starter = 0
    for row in matriz:
        for _ in range(0, len(matriz)):
            row.append(0)
        row[starter] = 1
        starter += 1
        print(row)

def ex003():
    """
    Faça um programa que preencha uma matriz 4x4 com o produto
    do valor da linha e da coluna de cada elemento. Em seguida,
    imprima na tela a matriz.
    """

    matriz = [[_, _, _, _] for _ in range(0, 4)]

    for row in matriz:
        for n in range(0, len(row)):
            row[n] = (matriz.index(row)+1) * (n+1)
        print(row)

def ex004():
    """
    Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e coluna)
    do maior valor
    """

    matriz = []
    for n in range(0, 4):
        tmp = []
        for _ in range(0, 4):
            tmp.append(
                int(input(f'Digite o {_+1}° valor para a {n+1}° linha da matriz: '))
            )
        print('===+===')
        matriz.append(tmp)

    line = 0
    row = 0
    hi = 0
    for n in range(0, 4):
        if n == 0:
            hi = max(matriz[n])
            row = matriz[n].index(hi) + 1
            line = n+1

        else:
            if max(matriz[n]) > hi:
                hi = max(matriz[n])
                row = matriz[n].index(hi) + 1
                line = n+1

    for r in matriz:
        print(r)

    print(f'O maior valor é {hi} e ele aparece na linha {line}, coluna {row}')

def ex005():
    """
    Leia uma matriz 5x5. Leia também um valor X. O programa deverá fazer
    uma busca desse valor na matriz e, ao final, escrever a localização
    (linha e coluna) ou uma mensagem de "não encontrado".
    """

    matriz = []
    for l in range(0, 5):
        tmp = []
        for n in range(0, 5):
            tmp.append(
                int(input(f'Digite o {n+1}° valor da {l+1}° linha: '))
            )
        matriz.append(tmp)
        print('===+===')

    for r in matriz:
        print(r)

    x = int(input('Digite o valor a ser procurado na matriz: '))
    line_num = 1
    x_is_found = False
    for line in matriz:
        if x in line:
            print(f'{x} foi encontrado primeiro na linha {line_num}, coluna {line.index(x) + 1}')
            x_is_found = True
            break

        else:
            line_num += 1

    if not x_is_found:
        print(f'O número {x} não foi achado na matriz!')

def ex006():
    """
    Leia duas matrizes 4x4 e escreva uma terceira com os maiores
    valores de cada posição das matrizes lidas.
    """

    matriz1 = []
    for l in range(0, 4):
        tmp = []
        for n in range(0, 4):
            tmp.append(
                int(input(f'Digite o {n+1}° valor para a linha {l+1} da matriz 1: '))
            )
        matriz1.append(tmp)
        print('---')

    matriz2 = []
    for l in range(0, 4):
        tmp = []
        for n in range(0,4):
            tmp.append(
                int(input(f'Digite o {n+1}° valor para a linha {l+1} da matriz 2: '))
            )
        matriz2.append(tmp)
        print('---')

ex006()

# KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
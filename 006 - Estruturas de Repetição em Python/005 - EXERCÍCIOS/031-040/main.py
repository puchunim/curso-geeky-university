def ex031(): # pulado porque eu sou burro
    """
    Faça um programa que calcule e escreva
    o valor de S
        S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
    """


def ex032():
    """
    Faça um programa que simula o lançamento de dois dados,
    d1 e d2, n vzes, e tem como saída o número de cada dado
    e a relação entre eles (>, <, =) de cada lançamento.
    """

    from random import randint

    while True:
        v = int(input('Digite quantas vezes os dois dados vão ser rolados: (Tem que ser positivo e maior de 0) '))
        if v > 0:
            break
    
    for d in range(1, v+1):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        if d1 > d2:
            simb = '>'
        
        else:
            simb = '<'

        print(f'{d}° roll: {d1}, {d2} ({d1} {simb} {d2})')


def ex033():
    """
    Dados 'n' e dois números inteiros positivos 'i' e 'j', diferentes de 0,
    imprimir em ordem crescente os 'n' primeiros naturais
    que são múltiplos de 'i' ou de 'j' e ou ambos. Ex:
        Para n = 6, i = 2 e j = 3, a saída deverá ser: 0, 2, 3, 4, 6 e 8.
    """

    while True:
        n = int(input('Digite um valor para n, inteiro e maior que 0: '))
        if n > 0:
            break
    
    while True:
        i = int(input('Digite um valor para i, inteiro e maior que 0: '))
        if i > 0:
            break

    while True:
        j = int(input('Digite um valor para j, inteiro e maior que 0: '))
        if j > 0:
            break
    
    print(f'Os primeiros {n} múltiplos são: ', end='')
    nat = 0
    multiplos = 0
    while not multiplos == n:
        if nat % i == 0 or nat % j == 0:
            multiplos += 1
            print(f'{nat} ', end='')
        nat += 1


def ex034(): # pulado porque to sem saco
    """
    Faça um programa que calcule o menor número divisível
    por cada um dos números de 1 a 20. Ex:
        2520 é o menor número que pode ser dividido por cada um
        dos números de 1 a 10, sem sobrar resto.
    """

# ZZZZZZZZZZZZZZ
# acho que eu vou quitar
# algum dia faço tudo
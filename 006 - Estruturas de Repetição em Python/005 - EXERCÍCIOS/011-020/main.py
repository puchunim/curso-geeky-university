def ex011():
    """
    Faça um um programa que leia um número
    inteiro positivo N e imprima todos os
    números naturais de 0 até N em ordem crescente.
    """

    while True:
        num = int(input('Digite um número natural positivo maior que 0: '))
        if num > 0:
            break
    
    print(f'Os números naturais de 0 até {num} são:')
    for n in range(0, num+1):
        print(n)


def ex012():
    """
    Faça um programa que leia um número
    inteiro positivo N e imprima todos os
    números naturais de 0 até N em ordem de-
    crescente.
    """

    while True:
        num = int(input('Digite um número natural positivo maior que 0: '))
        if num > 0:
            break
    
    print(f'Os números naturais de 0 até {num}, em ordem decrescente, são:')
    for n in range(num, -1, -1):
        print(n)


def ex013():
    """
    Faça um programa que leia um número
    inteiro positivo par N e imprima todos
    os números pares de 0 até N em ordem crescente.
    """

    while True:
        num = int(input('Digite um número positivo par e diferente de 0: '))
        if num % 2 == 0 and num > 0:
            break
    
    print(f'Números pares de 0 a {num}: ')
    for n in range(0, num+2, 2):
        print(n)


def ex014():
    """
    Faça um programa que leia um número
    inteiro positivo par N e imprima todos
    os números pares de 0 até N em ordem decrescente.
    """

    while True:
        num = int(input('Digite um número positivo par e diferente de 0: '))
        if num % 2 == 0 and num > 0:
            break
    
    print(f'Números pares de {num} a 0: ')
    for n in range(num,-2, -2):
        print(n)


def ex015():
    """
    Faça um programa que leia um número
    inteiro positivo ímpar N e imprima 
    todos os números ímpares de 1 a N em ordem
    crescente
    """

    while True:
        num = int(input('Digite um número inteiro impar diferente de 0: '))
        if num % 2 != 0 and num > 0:
            break
    
    print(f'Números impares de 1 a {num}:')
    for n in range(0, num+1):
        if n % 2 != 0:
            print(n)


def ex016():
    """
    Faça um programa que leia um número
    inteiro positivo ímpar N e imprima 
    todos os números ímpares de 1 a N em ordem
    decrescente
    """

    while True:
        num = int(input('Digite um número inteiro impar diferente de 0: '))
        if num % 2 != 0 and num > 0:
            break
    
    print(f'Números impares de {num} a 1:')
    for n in range(num, -1, -1):
        if n % 2 != 0:
            print(n)


def ex017():
    """
    Faça um programa que leia um número
    inteiro positivo N e calcule a soma dos
    N primeiros números naturais.
    """

    while True:
        num = int(input('Digite um número positivo inteiro e diferente de 0: '))
        if num > 0:
            break
    
    soma = 0
    for n in range(1, num+1):
        soma += n
    
    print(f'A soma total dos números naturais de 1 a {num} é: {soma}')


def ex018():
    """
    Escreva um algoritmo que leia certa quantidade
    de números e imprima o maior deles e quantas ve-
    zes o maior número lido. A quantidade de números
    a serem lidos deve ser fornecida pelo usuário.
    """

    while True:
        num = int(input('Digite um número inteiro e positivo maior que 0: '))
        if num > 0:
            break
    
    times = 0
    for n in range(0, num):
        while True:
            v = int(input(f'Digite o {n+1}° número: '))
            if v > 0:
                break

        if n == 0:
            maior = v
            times += 1
        
        if n != 0 and v > maior:
            maior = v
            times = 1
        
        elif n != 0 and v == maior:
            times += 1

    print(f'O maior número é {maior} e ele aparece {times} vezes!')


def ex019():
    """
    Escreva um algoritmo que leia um número
    inteiro entre 100 e 999 e imprima cada
    um dos algarismos que compõem o número.
    """

    while True:
        num = int(input('Digite um número entre 100 e 999: '))
        if num >= 100 and num <= 999:
            break
    
    print('Os algoritmos que compõem o número digitado são: ', end='')
    for a in str(num):
        print(a + ' ', end='')


def ex020(): # ?
    """
    Le uma sequência de números inteiros e
    determinar se eles são pares. Deverá ser
    informado o número de dados lidos quando for
    digitado o número 1000
    """

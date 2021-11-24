def ex021():
    """
    Faça um programa que receba dois números. Calcule e mostre:
    - A soma dos números pares desse intervalo de números, incluindo
    os números digitados.
    - A multiplicação dos números ímpares desse intervalo,
    incluindo os digitados.
    """

    while True:
        num1 = int(input('Digite um número inteiro positivo, maior que 0: '))
        if num1 > 0:
            break
    
    while True:
        num2 = int(input('Digite outro número inteiro positivo, maior que 0: '))
        if num2 > 0:
            break
    
    soma = 0
    for n in range(num1, num2+1):
        if n % 2 == 0:
            soma += n
    
    multi = 1
    for n in range(num1, num2):
        if n % 2 != 0:
            multi *= n

    print(f'A soma de todos os números paros nesse espaço é: {soma}')
    print(f'A multiplicação de todos os números ímpares nesse espaço é: {multi}')


def ex022():
    """
    Escreva um programa completo que permita a qualquer aluno
    introduzir, pelo teclado, uma sequência arbitrária de notas
    (válidas no intervalo de 10 a 20) e que mostre na tela, como
    resultado, a correspondente média aritmética. O número de notas
    com que o aluno pretenda efetuar o cálculo não será fornecido ao
    programa, o qual terminará quando for introduzido um valor que não
    seja válido como nota de aprovação.
    """

    total = 0
    vez = 0
    while True:
        tmp = int(input(f'Digite a {vez+1}° nota: '))
        if tmp < 10 or tmp > 20:
            break
        
        total += tmp
        vez += 1

    if vez == 0:
        print('Você só digitou um número, não dá pra tirar a média!')
    
    else:
        print(f'A média dos valores digitados é: {total / vez}')


def ex023():
    """
    Faça um algoritmo que leia um número
    positivo e imprima seus divisores.
    """

    while True:
        num = int(input('Digite um número positivo maior do que 0: '))
        if num > 0:
            break

    print(f'Os divisores de {num} são: ')
    for n in range(1, num+1):
        if num % n == 0:
            print(n)


def ex024():
    """
    Escreva um programa que leia um número inteiro
    e calcule a soma de todos os divisores desse
    número, com exceção dele próprio. 
    """

    while True:
        num = int(input('Digite um número inteiro positivo, maior que 0: '))
        if num > 0:
            break
    
    soma = 0
    for n in range(1, num):
        if num % n == 0:
            soma += n
    
    print(f'A soma de todos os divisores de {num} é: {soma}')


def ex025():
    """
    Faça um programa que some todos os números
    naturais abaixo de 1000 que são múltiplos de
    3 ou 5.
    """

    soma = 0
    print('A soma de todos os números naturais abaixo de 1000, múltiplos de 3 e 5 é: ', end='')
    for n in range(1, 1000):
        if n % 3 == 0 or n % 5 == 0:
            soma += n

    print(f'A soma total é igual a {soma}')


def ex026(): # Funciona mas tem um erro por causa do enunciado
    """
    Faça um algoritmo que encontre o primeiro múltiplo
    de 11, 13 ou 17 após um número dado.
    """
    pri_11 = 0
    pri_13 = 0
    pri_17 = 0

    while True:
        num = int(input('Digite um número positivo maior que zero: '))
        if num > 0:
            break
    
    for n in range(1, num+1):
        if 11 % n == 0:
            if pri_11 == 0:
                pri_11 = n
        
        elif 13 % n == 0:
            if pri_13 == 0:
                pri_13 = n
        
        elif 17 % n == 0:
            if pri_17 == 0:
                pri_17 = n
    
    print(f'Os primeiros múltiplos são:')
    if pri_11 == 0:
        print('Não foi achado múltiplo de 11')
    
    else:
        print(f'Primeiro múltiplo de 11: {pri_11}')
    
    if pri_13 == 0:
        print('Não foi achado múltiplo de 13')
    
    else:
        print(f'Primeiro múltiplo de 13: {pri_13}')
    
    if pri_17 == 0:
        print('Não foi achado múltiplo de 17')
    
    else:
        print(f'Primeiro múltiplo de 17: {pri_17}')
        

def ex027():
    """
    Em matemática, o número harmônico designado por
    H(n) define-se como sendo a soma da série harmônica:
        H(n) = 1 + 1/2 + 1/3 + 1/4 + 1/n
    Faça um programa que leia um valor n e apresente
    o valor de H(n)
    """

    while True:
        n = int(input('Digite um número inteiro e maior que 0: '))
        if n > 0:
            break
    
    h = 1
    for nh in range(2, n+1):
        h += (1/nh)

    print(f'O valor de H(n), sendo n = {n}, é: {h}')


def ex028():
    """
    Faça um programa que leia um valor N inteiro e positivo,
    calcule e mostre o valor de N conforme a fórmula à seguir.
        E = 1 + 1/1! + 1/2! + 1/3! + 1/N!
    """

    while True:
        n = int(input('Digite um valor inteiro positivo e maior do que 0: '))
        if n > 0:
            break
    
    e = 0
    for v in range(n, 0, -1):
        tmp = 1
        for f in range(v, 0, -1):
            tmp *= f
        e += (v/tmp)
    
    print(f'O valor de E é {e}!')


def ex029():
    """
    Escreva um programa para calcular
    o valor da série, para 5 termos.
        S = 0 + 1/2! + 2/4! + 3/6! + ...
    """

    while True:
        n = int(input('Digite um número inteiro, positivo e maior que 0: '))
        if n > 0:
            break
    
    s = 0
    for t in range(n, n+5):
        tmp = 1
        for f in range((t*2), 0, -1):
            tmp *= f
        s += t/tmp
    
    print(f'O valor dos 5 primeiros termos da sequência começada em {n} é: {s}!')


def ex030(): # Só funciona a primeira e a terceira sequência
    """
    Faça um programa para calcular as seguintes
    sequências:
        1 + 2 + 4 + 5 + ... + n
        1 - 2 + 3 - 4 - 5 + ... + (2n - 1)
        1 + 3 + 5 + 7 + ... + (2n - 1)
    """

    while True:
        n = int(input('Digite um número inteiro e positivo maior que 0: '))
        if n > 0:
            break
    
    print('Sequência 1: ')
    s1 = 0
    for _ in range(1, n+1):
        if _ < n: 
            print(f'{_} + ', end='')
        
        else:
            print(f'{_} = ', end='')
        s1 += _
    print(f'{s1}!\n\n')

    print('Sequência 2: ')
    s2 = 0


    print('Sequência 3: ')
    s3 = 0
    for _ in range(1, n+1, 2):
        if _ < n:
            print(f'{_} + ', end='')
        
        else:
            print(f'{_} = ', end='')
        s3 += _
    
    print(f'{s3}!\n\n')
